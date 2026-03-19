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
    write("death bless me", 0.06, "blue")
    write("with you", 0.11, "blue")
    write("Whooaa-oh", 0.11, "blue")
    time.sleep(1)
    console.print()
    write("would  you die tonight for love?", 0.08)
    time.sleep(2)
    write("Baby, join me in death", 0.07)
    console.print()
    time.sleep(1)
    write("So, would you die?????", 0.07,"blue") 
    console.print()
    time.sleep(2)
    write("Baby, join me in death...", 0.11)

    time.sleep(2)
    console.print()
  
    clear()


sing()