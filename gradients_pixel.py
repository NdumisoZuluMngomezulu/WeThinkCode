'''
To create an undithered linear gradient between two points in the standard sRGB color space using only pure Python, you must account for the sRGB gamma correction. Direct linear interpolation of the sRGB color values (0-255) results in a perceptually non-linear gradient (it appears to pass through gray). 
The correct approach involves these steps:
Convert sRGB integer values (0-255) to linear sRGB float values (0.0-1.0).
Linearly interpolate the colors in this linear space.
Convert the resulting linear float values back to non-linear sRGB integer values
'''

import math

def srgb_to_linear(c_srgb):
    """Convert a single 0-255 sRGB value to a 0.0-1.0 linear value."""
    c_srgb /= 255.0
    if c_srgb <= 0.04045:
        c_linear = c_srgb / 12.92
    else:
        c_linear = ((c_srgb + 0.055) / 1.055) ** 2.4
    return c_linear

def linear_to_srgb(c_linear):
    """Convert a single 0.0-1.0 linear value back to a 0-255 sRGB value."""
    if c_linear <= 0.0031308:
        c_srgb = c_linear * 12.92
    else:
        c_srgb = 1.055 * (c_linear ** (1.0/2.4)) - 0.055
    return int(max(0, min(255, round(c_srgb * 255.0))))

def create_linear_gradient_pixels(x1, y1, r1, g1, b1, x2, y2, r2, g2, b2):
    """
    Creates a list of (x, y, r, g, b) tuples for an undithered linear gradient 
    between two points (x1, y1) and (x2, y2) with specified sRGB colors (r, g, b).
    Uses the sRGB gamma curve for perceptually uniform interpolation.
    """
    # Calculate the distance and number of steps (pixels)
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)
    
    if distance == 0:
        return [(x1, y1, r1, g1, b1)]

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

# --- Example Usage ---
# Start point (x, y) = (10, 20), color = Red (255, 0, 0)
# End point (x, y) = (110, 70), color = Blue (0, 0, 255)
gradient_pixels = create_linear_gradient_pixels(10, 20, 255, 0, 0, 110, 70, 0, 0, 255)

# Print the first few and last few pixels
print("First 5 pixels:")
for p in gradient_pixels[:5]:
    print(f"  (x={p[0]}, y={p[1]}) -> RGB: ({p[2]}, {p[3]}, {p[4]})")

print("\nLast 5 pixels:")
for p in gradient_pixels[-5:]:
    print(f"  (x={p[0]}, y={p[1]}) -> RGB: ({p[2]}, {p[3]}, {p[4]})")
