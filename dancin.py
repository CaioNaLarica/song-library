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
    write("All the time", 0.07)
    write("My baby, you on my mind", 0.08,"green")
    console.print()
    write("And I don't know why", 0.07) 
    write("Yeah, but the feeling is fine", 0.07,"green")
    console.print()
    write("Can't you see?", 0.07) 

    write("Yo' honey you are for me, oh", 0.08, "green")
    console.print()
    time.sleep(0.4)
    write("We were meant to be 🎶", 0.06) 
    time.sleep(0.6)
    write("Dancin' in the moonlight", 0.09,"green")
    time.sleep(1.2)
    console.print()
    write("Gazing at the stars so bright", 0.1) 
    time.sleep(1)
    write("Holding you until the sunrise", 0.09,"green") 
    time.sleep(0.7)
    console.print()
    write("Sleeping until the midnight", 0.1) 



  
    

    time.sleep(2)
    
    clear()

sing()
    
