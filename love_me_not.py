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
    write("i need you right now", 0.04, "blue")
    write("once i leave you, i'm strung out", 0.04, "blue")
    write("if i get you, i'm slowly breaking down", 0.06,"blue")
    console.print()
    time.sleep(2)
    write("and oh, it's hard to see you", 0.04)
    write("but i wish you were right here", 0.04)
    write("oh, it's hard to leave you when i get you everywhere.", 0.06)
    write("all this time i'm thinking ", 0.05)
    write("we could never be a pair", 0.06)
    write("oh no, i don't need you", 0.05)
    write("but i miss you, come here", 0.07) 
    
    
    
    
    
    time.sleep(2)
    console.print()
  
 
    clear()


sing()