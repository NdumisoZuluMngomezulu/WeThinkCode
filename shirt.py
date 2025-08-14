import sys
from PIL import Image, ImageOps

def main():
    if (len(sys.argv) > 3):
        sys.exit("Too many arguments")
    elif (len(sys.argv) < 3):
        sys.exit("Too few arguments")
    elif ((sys.argv[1].endswith(".png")) or (sys.argv[1].endswith(".jpeg")) or (sys.argv[1].endswith(".jpg"))) and ((sys.argv[2].endswith(".png")) or (sys.argv[2].endswith(".jpeg")) or (sys.argv[2].endswith(".jpg"))):
        
        edit_image(sys.argv[1], sys.argv[2])
        
    else:
        sys.exit("Input does not exist")

def edit_image(input, output):
    firstIMG = Image.open(input)
    secondIMG = Image.open(output)
    shirtSIZE = firstIMG.size
    secondIMG = ImageOps.fit(secondIMG, shirtSIZE)
    secondIMG.past(firstIMG, mask = firstIMG)
    secondIMG.save(output)

if __name__ == "__main__":
    main()
