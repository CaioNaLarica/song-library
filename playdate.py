import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

def write(text, speed, cor="white"):
    linha = ""

    with Live("", console=console, refresh_per_second=20, transient=True) as live:
        for letra in text:
            linha += letra
            live.update(f"[{cor}]{linha}[/]")
            time.sleep(speed)

    console.print(f"[bold {cor}]{text}[/]")
    time.sleep(0.6)

def sing():
    clear()
    write("I guess I'm just a playdate to you", 0.08, "magenta") 
    console.print()
    time.sleep(1)
    write("You know I give a f-ck about you everyday", 0.1)
    time.sleep(0.2)
    write("Guess it's time that I tell you the truth", 0.09)
    console.print()
    time.sleep(0.5)
    write("If I share my toys, will you let me stay?", 0.09 ) 
    console.print()
    write("Don't wanna leave this playdate with you", 0.09,"magenta") 
    
    time.sleep(2)
    console.print()
    
    clear()

sing()\
    