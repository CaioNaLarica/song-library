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
    write("I wanna, I wanna rock right now", 0.07)
    time.sleep(1.5)
    write("I wanna da-, I wanna dance in the lights", 0.07,"blue")
    console.print()
    time.sleep(0.4)
    write("I wanna ro-, I wanna rock your body ", 0.07) 
    time.sleep(0.4)
    write("I wanna go, I wanna go for a ride ", 0.07)
    time.sleep(0.8)
    console.print()
    write("Hop in the music and rock your body", 0.1) 
    time.sleep(0.5)
    console.print()
    write("rock your body", 0.06) 


  
    

    time.sleep(2)
    
    clear()

sing()
    
