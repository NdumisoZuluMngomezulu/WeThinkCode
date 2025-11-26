import struct

def create_bmp(pixel_data, width, height, filename="output.bmp"):
    """
    Creates a 24-bit uncompressed BMP file with a 54-byte header.

    Args:
        pixel_data (list of lists): A 2D list representing pixel data in BGR format.
                                    Each inner list is a row of pixels, and each pixel
                                    is a tuple/list of (blue, green, red) values.
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.
        filename (str): The name of the BMP file to save.
    """

    # Calculate image size and padding
    bytes_per_pixel = 3
    row_size = width * bytes_per_pixel
    padding_bytes = (4 - (row_size % 4)) % 4  # BMP rows must be padded to a multiple of 4 bytes
    padded_row_size = row_size + padding_bytes
    image_size = padded_row_size * height

    # BMP File Header (14 bytes)
    bfType = b'BM'  # Signature
    bfSize = 54 + image_size  # File size in bytes
    bfReserved1 = 0
    bfReserved2 = 0
    bfOffBits = 54  # Offset to pixel data

    # DIB Header (BITMAPINFOHEADER - 40 bytes)
    biSize = 40  # Size of DIB header
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

    # Pack the headers
    bmp_header = struct.pack('<2sIHH', bfType, bfSize, bfReserved1, bfReserved2) + \
                 struct.pack('<I', bfOffBits)
    dib_header = struct.pack('<IiiHHIIIIII', biSize, biWidth, biHeight, biPlanes,
                             biBitCount, biCompression, biSizeImage, biXPelsPerMeter,
                             biYPelsPerMeter, biClrUsed, biClrImportant)

    # Write to file
    with open(filename, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)

        # Write pixel data with padding
        for row in reversed(pixel_data):  # BMP stores rows bottom-up
            for pixel in row:
                f.write(struct.pack('<BBB', pixel[0], pixel[1], pixel[2]))  # BGR order
            f.write(b'\x00' * padding_bytes)
