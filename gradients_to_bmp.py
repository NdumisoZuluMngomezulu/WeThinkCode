import struct
import math

def srgb_to_linear(c):
    """Convert sRGB value (0-255) to linear (0.0-1.0)."""
    c = c / 255.0
    if c <= 0.04045:
        return c / 12.92
    else:
        return ((c + 0.055) / 1.055) ** 2.4

def linear_to_srgb(c):
    """Convert linear value (0.0-1.0) to sRGB (0-255)."""
    if c <= 0.0031308:
        c *= 12.92
    else:
        c = 1.055 * (c ** (1.0 / 2.4)) - 0.055
    return max(0, min(255, int(c * 255.0 + 0.5))) # Add 0.5 for rounding

def create_gradient_bmp(filename, width, height, x1, y1, rgb1, x2, y2, rgb2):
    """
    Creates a 24-bit undithered linear gradient BMP file.

    Args:
        filename (str): The name of the output BMP file.
        width (int): Image width in pixels.
        height (int): Image height in pixels.
        x1, y1 (int): Coordinates of the starting point.
        rgb1 (tuple): RGB values (R, G, B) for the starting point (0-255).
        x2, y2 (int): Coordinates of the ending point.
        rgb2 (tuple): RGB values (R, G, B) for the ending point (0-255).
    """
    # Convert sRGB input colors to linear space
    linear_rgb1 = (srgb_to_linear(rgb1[0]), srgb_to_linear(rgb1[1]), srgb_to_linear(rgb1[2]))
    linear_rgb2 = (srgb_to_linear(rgb2[0]), srgb_to_linear(rgb2[1]), srgb_to_linear(rgb2[2]))

    # Calculate gradient vector parameters
    dx, dy = x2 - x1, y2 - y1
    dist_sq = dx**2 + dy**2
    
    if dist_sq == 0:
        # Handle case where points are the same
        dist_sq = 1
    
    # BMP files require rows to be padded to a 4-byte boundary.
    padding_size = (4 - (width * 3) % 4) % 4
    pixel_data_size = (width * 3 + padding_size) * height
    file_size = 54 + pixel_data_size # 54 bytes for headers

    # --- Create BMP headers ---
    # BITMAPFILEHEADER (14 bytes)
    bfType = b'BM'
    bfSize = struct.pack('<I', file_size)
    bfReserved1 = struct.pack('<H', 0)
    bfReserved2 = struct.pack('<H', 0)
    bfOffBits = struct.pack('<I', 54)

    # BITMAPINFOHEADER (40 bytes)
    biSize = struct.pack('<I', 40)
    biWidth = struct.pack('<i', width)
    biHeight = struct.pack('<i', height) # BMP stores pixels bottom-up, so height can be negative for top-down
    biPlanes = struct.pack('<H', 1)
    biBitCount = struct.pack('<H', 24)
    biCompression = struct.pack('<I', 0)
    biSizeImage = struct.pack('<I', pixel_data_size)
    biXPelsPerMeter = struct.pack('<i', 0)
    biYPelsPerMeter = struct.pack('<i', 0)
    biClrUsed = struct.pack('<I', 0)
    biClrImportant = struct.pack('<I', 0)

    bmp_header = (
        bfType + bfSize + bfReserved1 + bfReserved2 + bfOffBits +
        biSize + biWidth + biHeight + biPlanes + biBitCount +
        biCompression + biSizeImage + biXPelsPerMeter + biYPelsPerMeter +
        biClrUsed + biClrImportant
    )

    # --- Generate pixel data ---
    pixel_data = bytearray()
    for y in range(height):
        for x in range(width):
            # Calculate projection of current pixel onto the gradient vector
            # Parameter t ranges from 0 to 1 along the line segment
            t = max(0.0, min(1.0, ((x - x1) * dx + (y - y1) * dy) / dist_sq))

            # Linear interpolation in linear color space
            r_linear = linear_rgb1[0] + t * (linear_rgb2[0] - linear_rgb1[0])
            g_linear = linear_rgb1[1] + t * (linear_rgb2[1] - linear_rgb1[1])
            b_linear = linear_rgb1[2] + t * (linear_rgb2[2] - linear_rgb1[2])

            # Convert back to sRGB (0-255) for storage
            r_srgb = linear_to_srgb(r_linear)
            g_srgb = linear_to_srgb(g_linear)
            b_srgb = linear_to_srgb(b_linear)

            # BMP stores pixels in BGR order
            pixel_data.extend([b_srgb, g_srgb, r_srgb])
        
        # Add padding
        pixel_data.extend(b'\x00' * padding_size)

    # --- Write to file ---
    with open(filename, 'wb') as f:
        f.write(bmp_header)
        f.write(pixel_data)

# Example Usage:
# Create a 256x256 image with a gradient from top-left (0, 0, red) to bottom-right (255, 255, blue)
create_gradient_bmp(
    filename='srgb_gradient.bmp',
    width=256,
    height=256,
    x1=0, y1=0, rgb1=(255, 0, 0),
    x2=255, y2=255, rgb2=(0, 0, 255)
)

print("Saved 'srgb_gradient.bmp'")
