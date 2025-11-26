'''
To create an undithered linear gradient between two points in the standard sRGB color space using only pure Python, you must account for the sRGB gamma correction. Direct linear interpolation of the sRGB color values (0-255) results in a perceptually non-linear gradient (it appears to pass through gray). 
The correct approach involves these steps:
Convert sRGB integer values (0-255) to linear sRGB float values (0.0-1.0).
Linearly interpolate the colors in this linear space.
Convert the resulting linear float values back to non-linear sRGB integer values
'''

import argparse
import math
import struct
import sys

def points_validator(points):
    first_point = points[0]
    second_point = points[1]
    coordinates1, colors1 = first_point.split("=")
    x1, y1 = coordinates1.split(",")
    red1, green1, blue1 = colors1.split(",")
    
    red1 = 0 if float(red1) < 0 else float(red1)
    red1 = 255 if float(red1) > 255 else float(red1)
    green1 = 0 if float(green1) < 0 else float(green1) 
    green1 = 255 if float(green1) > 255 else float(green1)
    blue1 = 0 if float(blue1) < 0 else float(blue1) 
    blue1 = 255 if float(blue1) > 255 else float(blue1)

    first_tuple = (float(x1), float(y1), red1, green1, blue1)

    coordinates2, colors2 = second_point.split("=")
    x2, y2 = coordinates2.split(",")
    red2, green2, blue2 = colors2.split(",")
    
    red2 = 0 if float(red2) < 0 else float(red2)
    red2 = 255 if float(red2) > 255 else float(red2)
    green2 = 0 if float(green2) < 0 else float(green2) 
    green2 = 255 if float(green2) > 255 else float(green2)
    blue2 = 0 if float(blue2) < 0 else float(blue2) 
    blue2 = 255 if float(blue2) > 255 else float(blue2)

    second_tuple = (float(x2), float(y2), red2, green2, blue2)
    print([first_tuple, second_tuple])

    return [first_tuple, second_tuple]
 

def srgb_to_linear(c_srgb):
    print(f"+++{c_srgb}")
    c_srgb = float(c_srgb)
    """Convert a single 0-255 sRGB value to a 0.0-1.0 linear value."""
    c_srgb /= 255.0
    if c_srgb <= 0.04045:
        c_linear = c_srgb / 12.92
    else:
        c_linear = ((c_srgb + 0.055) / 1.055) ** 2.4
    return c_linear

def linear_to_srgb(c_linear):
    print(f"+++{c_srgb}")
    c_srgb = float(c_srgb)
    """Convert a single 0.0-1.0 linear value back to a 0-255 sRGB value."""
    if c_linear <= 0.0031308:
        c_srgb = c_linear * 12.92
    else:
        c_srgb = 1.055 * (c_linear ** (1.0/2.4)) - 0.055
    return int(max(0, min(255, round(c_srgb * 255.0))))
    
def create_linear_gradient_pixels(first_tuple, second_tuple):
    print(first_tuple)
    x1 = first_tuple[0]
    y1 = first_tuple[1]
    r1 = first_tuple[2]
    g1 = first_tuple[3]
    b1 = first_tuple[4]
    x2 = second_tuple[0]
    y2 = second_tuple[1]
    r2 = second_tuple[2]
    g2 = second_tuple[3]
    b2 = second_tuple[4]
    """
    Creates a list of (x, y, r, g, b) tuples for an undithered linear gradient 
    between two points (x1, y1) and (x2, y2) with specified sRGB colors (r, g, b).
    Uses the sRGB gamma curve for perceptually uniform interpolation.
    """
    # Calculate the distance and number of steps (pixels)
    dx = float(x2) - float(x1)
    dy = float(y2) - float(y1)
    distance = math.sqrt(dx**2 + dy**2)
    
    if distance == 0:
        return [(x1, y1, r1, g1, b1)]
    print(r1)
    print(b1)

    # Convert start/end colors to linear space (0.0-1.0 range)
    c1_linear = (srgb_to_linear(r1), srgb_to_linear(g1), srgb_to_linear(b1))
    c2_linear = (srgb_to_linear(r2), srgb_to_linear(g2), srgb_to_linear(b2))

    pixels = []
    # Iterate over each pixel along the line
    # (A simple approach, actual line drawing algorithms like Bresenham might be better 
    # for rendering on a canvas, but this works for calculation)
    for i in range(int(distance) + 1):
        t = i / distance # Interpolation factor (0.0 to 1.0)

        # Interpolate in linear space
        r_linear = c1_linear[0] * (1.0 - t) + c2_linear[0] * t
        g_linear = c1_linear[1] * (1.0 - t) + c2_linear[1] * t
        b_linear = c1_linear[2] * (1.0 - t) + c2_linear[2] * t

        # Convert back to sRGB integer values (0-255)
        r_srgb = linear_to_srgb(r_linear)
        g_srgb = linear_to_srgb(g_linear)
        b_srgb = linear_to_srgb(b_linear)

        # Calculate coordinates (rounding to nearest integer for pixel grid)
        x = round(x1 + t * dx)
        y = round(y1 + t * dy)

        pixels.append((int(x), int(y), r_srgb, g_srgb, b_srgb))
    
    return pixels

def create_bmp(pixels, width=100, height=100, filename="output.bmp"):
    """
    Creates a 24-bit uncompressed BMP file with a 54-byte header.
    Pixels is list of lists representing pixel data in BGR format. Each inner list is a row of pixels, and each pixel is a tuple/list of (blue, green, red) values.
    """

    #image size and padding
    bytes_per_pixel = 3
    row_size = width * bytes_per_pixel
    padding_bytes = (4 - (row_size % 4)) % 4  # BMP rows must be padded to a multiple of 4 bytes
    padded_row_size = row_size + padding_bytes
    image_size = padded_row_size * height

    # BMP File Header
    bfType = b'BM'  
    bfSize = 54 + image_size  # File size in bytes
    bfReserved1 = 0
    bfReserved2 = 0
    bfOffBits = 54  # Offset to pixel data

    # DIB Header
    biSize = 40  
    biWidth = width
    biHeight = height
    biPlanes = 1
    biBitCount = 24  # 24 bits per pixel (RGB)
    biCompression = 0  # No compression
    biSizeImage = image_size
    biXPelsPerMeter = 0
    biYPelsPerMeter = 0
    biClrUsed = 0
    biClrImportant = 0

    bmp_header = struct.pack('<2sIHH', bfType, bfSize, bfReserved1, bfReserved2) + \
                 struct.pack('<I', bfOffBits)
    dib_header = struct.pack('<IiiHHIIIIII', biSize, biWidth, biHeight, biPlanes,
                             biBitCount, biCompression, biSizeImage, biXPelsPerMeter,
                             biYPelsPerMeter, biClrUsed, biClrImportant)

    with open(filename, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)

        for row in reversed(pixels):  # BMP stores rows bottom-up
            for pixel in row:
                f.write(struct.pack('<BBB', pixel[0], pixel[1], pixel[2]))  # BGR order
            f.write(b'\x00' * padding_bytes)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="")
    parser.add_argument("points", nargs="+", help="")

    args = parser.parse_args()
    points = points_validator(args.points)
    print(points[0])
    pixels = create_linear_gradient_pixels(args.points[0], args.points[1])
    create_linear_gradient_pixels(pixels, width=100, height=100, filename = args.output)
