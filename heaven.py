import time
import sys

AZUL_CLARO = "\033[96m"
RESET = "\033[0m"

def write(text, speed, color=AZUL_CLARO):
    for lyrics in text:
        sys.stdout.write(color + lyrics + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()
    time.sleep(0.6)

def sing():
    write("You keep me coming back for more", 0.09)
    print()
    write("Baby, you're all that I want", 0.09)
    write("When you're lying here in my arms", 0.08)
    write("I'm finding it hard to believe", 0.09)
    write("We're in heaven", 0.07)
    print()
    write("         ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♬", 0.06)
    write("And love is all that I need", 0.09)
    write("And I found it there in your heart", 0.08)
    write("It isn't too hard to see", 0.1)
    write("We're in heaven", 0.08)
    write("         ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♬", 0.06)

sing()