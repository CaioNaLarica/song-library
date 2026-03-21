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
    write("you know", 0.12, "yellow")
    write("you know where", 0.11, "yellow")
    write("you are with", 0.12, "yellow") 
    
    console.print()
    
    write("you know where", 0.12, "yellow")
    write("you are with", 0.12, "yellow")
    clear()
    
    console.print()
    
    write("floor collapsing", 0.12, "yellow")
    write("floating", 0.17, "yellow")
    time.sleep(0.4)
    write("bouncing back", 0.16, "yellow")
    
    write("and one day", 0.13, "yellow")
    time.sleep(0.6)
    write("i am gonna grow wings...", 0.15, "yellow")
    
    time.sleep(2)
    console.print()
    
    clear()

sing()\
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
