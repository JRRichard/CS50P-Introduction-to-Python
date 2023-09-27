import sys
import random
from pyfiglet import Figlet


figlet = Figlet()
fonts = figlet.getFonts()
calls = ["-f", "--font"]


if len(sys.argv) == 1:
    words = input("Input: ")
    f = random.choice(fonts)
    figlet.setFont(font = f)
    print(figlet.renderText(words))

# Exit if length of sys.argv is only 2 or doesn't start with -f or --font or font not in list
if len(sys.argv)>1:
    if len(sys.argv) == 2 or sys.argv[1] not in calls or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    elif len(sys.argv)==3:
        words = input("Input: ")
        f = sys.argv[2]
        figlet.setFont(font = f)
        print(figlet.renderText(words))


