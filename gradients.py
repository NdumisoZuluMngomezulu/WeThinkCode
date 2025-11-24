import argparse

def points_validator(points):
    first_point , second_point = points.strip().split(" ")
    coordinates1, colors1 = first_point.split("=")
    x1, y1 = coordinates1.split(",")
    red1, green1, blue1 = colors1.split(",")
    
    red1 = 0 if red1 < 0 else red1
    red1 = 255 if red1 > 255 else red1
    green1 = 0 if green1 < 0 else green1 
    green1 = 255 if green1 > 255 else green1
    blue1 = 0 if blue1 < 0 else blue1 
    blue1 = 255 if blue1 > 255 else blue1

    first_tuple = (x1, y1, red1, blue1, green1)

    coordinates2, colors2 = second_point.split("=")
    x2, y2 = coordinates2.split(",")
    red1, green1, blue1 = colors2.split(",")
    
    red2 = 0 if red2 < 0 else red2
    red2 = 255 if red2 > 255 else red2
    green2 = 0 if green2 < 0 else green2 
    green2 = 255 if green2 > 255 else green2
    blue2 = 0 if blue2 < 0 else blue2 
    blue2 = 255 if blue2 > 255 else blue2

    second_tuple = (x2, y2, red2, blue2, green2)

    return [first_tuple, second_tuple]
 
def bit_generator(points):
    pass

def header():
    pass

def infoheader():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="")
    parser.add_argument("points", nargs="+", help="")

    args = parser.parse_args()
    points = points_validator(args.points)
    bits = bit_generator(args.points)

    with open(args.output, "wb") as file:
        file.write(header())
        file.write(infoheader())
        file.write(bits)
