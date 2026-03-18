import time
import sys
import os

ROXO =  "\033[95m"
CINZA = "\033[90m"
RESET = "\033[0m"
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def write(text, speed):
    for i in range(len(text) + 1):
        parte = text[:i]
        resto = text[i:]
        
        sys.stdout.write("\r" + " " * len(text))
        sys.stdout.write("\r")
        
        sys.stdout.write(ROXO + parte + CINZA + resto + RESET)
        sys.stdout.flush()
        
        time.sleep(speed)
    
    print()
    time.sleep(0.6)

def sing():
    clear()
    write("A night that they never forget", 0.09)
    print()

    write("Touch me, yeahh", 0.13)
    time.sleep(2)
    clear()
    write("I want you to touch me there", 0.1)
    time.sleep(2)

    write("Make me feel like I am breathing", 0.11)
    time.sleep(2)

    write("Feel like I am human", 0.18)
    time.sleep(2)
    print()

sing()