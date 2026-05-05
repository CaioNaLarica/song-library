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
    write("Um amor tão puro que ainda nem sabe", 0.09)
    write("A força que tem", 0.09)
    console.print()
    time.sleep(1)
    write("É teu e de mais ninguém", 0.08, "blue" ) 
    time.sleep(2.5)
    write("Te adoro em tudo, tudo, tudo", 0.09) 
    time.sleep(1)
    write("Quero mais que tudo, tudo, tudo", 0.08)
    console.print()
    time.sleep(1) 
    write("Te amar sem limites", 0.08, "blue") 
    write("Viver uma grande história", 0.11) 
    console.print()
  


    time.sleep(3)
    
    clear()

sing()
    
