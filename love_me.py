
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
    write("She's on a strict diet, that's my baby", 0.07, "blue" )
    time.sleep(0.3)
    write("With no makeup, she a ten", 0.06)
    console.print()
    write("And she the best with that head, even better than Karrine", 0.05, "blue" ) 
    write("She don't want money", 0.05) 
    write("She want the time that we could spend", 0.05, "blue" )
    console.print()
    write("She said: 'Cause I really need somebody",  0.04) 
    write("So tell me you're that somebody", 0.03) 
    console.print()
    write("Girl, I fuck who I want",  0.04, "blue") 
  
    

    time.sleep(2)
    
    clear()

sing()