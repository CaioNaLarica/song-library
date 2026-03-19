import time
import os
from rich.console import Console

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

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
    write("We don't talk anymore", 0.06, "yellow")
    write("Like we used to do", 0.11, "yellow")
    console.print()
    write("I overdosed", 0.14)
    write("Should've known your love was a game", 0.07)
    console.print()
    write("Now I can't get you out of my brain", 0.07)
    write("Oh, it's such a shamed...", 0.1)
    time.sleep(2)
    console.print()
    clear()


sing()