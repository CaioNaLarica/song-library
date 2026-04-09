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
    write("Spend some time alone", 0.09)
    time.sleep(1.3)
    write("Understand that soon you'll run with better men", 0.09,"blue")
    console.print()
    time.sleep(1.5)
    write("Alone again", 0.12) 
    time.sleep(1.5)
    write("Alone again", 0.12,"blue") 
    time.sleep(1.5)
    console.print()
    write("Alone again", 0.12) 
    time.sleep(1.5)
    write("Alone again", 0.12,"blue")
    time.sleep(1.5)
    console.print()
    write("Alone again", 0.12) 
    

  
    

    time.sleep(2)
    
    clear()

sing()
    
