import time
import sys
import os


BRANCO = "\033[97m"
CINZA = "\033[90m"
RESET = "\033[0m"

def write(text, speed):
    for i in range(len(text) + 1):
        parte = text[:i]
        resto = text[i:]
        
        
        sys.stdout.write("\r" + " " * len(text))
        sys.stdout.write("\r")
        
        sys.stdout.write(BRANCO + parte + CINZA + resto + RESET)
        sys.stdout.flush()
        
        time.sleep(speed)
    
    print()
    time.sleep(0.6)
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def sing():
    clear()
    write("now look at what you've done to me", 0.04)
    time.sleep(1)
    write("i used to let them step on my vertebrae", 0.04)
    time.sleep(1)

    write("and now im the one skipping, and laughing, and cheering", 0.05)
    write("its baffing how magic works", 0.05) 

    write("I mean I lit a candle for this", 0.05) 
    write("burned some bay leaves for this ", 0.03)

    write("cried to god for this", 0.02)
    clear()
    write("AHHHHHHHHHHHH", 0.03)
    write("to turn me into", 0.04)
    write("i don't give a single flying ", 0.05)
    write("fuckity fuck fuck fuck machine", 0.04)
    time.sleep(1)
    clear()
    write("basic aren't ya santa monica", 0.07)

    write("pale white skin like antartictica", 0.07)
    write("my angels put a hex on you", 0.09)
    write("guess they had a grudge too", 0.09)


sing()