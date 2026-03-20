import time
import os
from rich.console import Console

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
def write(text, speed, cor="white"):
    linha = ""

    for letra in text:
        linha += letra
        console.print(f"[{cor}]{linha}[/]", end="\r")
        time.sleep(speed)

    console.print(f"[bold {cor}]{text}[/]")
    time.sleep(0.6)

def sing():
    clear()
    write("You know you're better than this", 0.05, "red")
    console.print()
    write("You say too late to start", 0.05)
    write("Got your heart in a headlock", 0.05)
    time.sleep(2)
    write("I don't believe any of it", 0.07)
    write("You say too late to start", 0.06)
    write("With your heart in a headlock", 0.08)
    console.print()
    write("You know you're better than this", 0.09, "red")
 
    clear()


sing()