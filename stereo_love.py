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
    write("I hate to see you cry, my love is dyin' inside", 0.06)
    time.sleep(0.2)
    write("I can fix all those lies", 0.08, "blue" ) 
    console.print()
    write("Oh-baby, babe, I run, but I'm runnin' to you", 0.06) 
    console.print()
    write("You won't see me cry, I'm hidin' inside", 0.07, "blue" )
    console.print()
    write("My heart is in pain, but I'm smilin' for you 🎶", 0.08) 
    time.sleep(2)
    
    clear()

sing()