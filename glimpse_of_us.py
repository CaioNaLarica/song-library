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
    write("'Cause sometimes i look in her eyes", 0.09, "red")
    write("and that's where i find", 0.07)
    write("a glimpse of us ", 0.08 ) 
    time.sleep(0.4)
    write("and i try to fall for her touch", 0.1 ) 
    write("but i'm thinking of the way it was", 0.09) 
    time.sleep(1)
    write("Said \"I'm fine\"", 0.08, "red")
    time.sleep(0.3)
    write("Said \"I moved on\"", 0.08, "red")
    write("i'm only here passing time in her arms", 0.09)
    write("hoping l'll find", 0.12) 
    time.sleep(0.8)
    console.print()
    write("a glimpse of us", 0.18, "red")
    
    time.sleep(2)

    
    clear()

sing()\
    
