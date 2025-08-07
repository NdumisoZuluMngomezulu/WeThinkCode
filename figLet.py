from pyfiglet import Figlet
import sys
import random

def ASCIIfigLET():
    figures= Figlet()
    fontlist = figures.getFonts()

    Fonts = 'temp'

    if len(sys.argv) == 1:
        Fonts = fontlist[random.randint(1,424)]
    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "-font") and sys.argv[2] in fontlist:
            Fonts = sys.argv[2]
        else:
            sys.exit("Incorect arguments, will halt")
    else:
        sys.exit("Too many argument, will halt.")

    text = input("Input: ")

    try:
        if Fonts in fontlist:
            figures.setFont(font=Fonts)
            print(figures.renderText(text))
    except:
        sys.exit("Error")

ASCIIfigLET()
