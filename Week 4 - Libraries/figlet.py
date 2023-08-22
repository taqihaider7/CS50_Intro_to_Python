# importing important libraries
import sys
import random
from pyfiglet import Figlet
# defining main function
def main():
    # definignfilet object
    figlet = Figlet()
    # when user don't give any argument ---> by default fie4st argument is figlet.py itself
    if len(sys.argv) == 1:
        fonts = figlet.getFonts()   # getting the fonts
        font = random.choice(fonts)     # chossing random font using Random Library
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:   # user provide two arguments first one from the
                                                                   # ["-f", "--font"] and second one name of font
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")   # user's both two arguments doesnot match. program will exit
    figlet.setFont(font=font)   # setting the font
    text = input("Input: ")         # asking input from user
    print("Output:",figlet.renderText(text))   # showing output

if __name__ == "__main__":
    main()