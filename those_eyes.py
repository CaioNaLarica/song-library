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
    write("'Cause all of the small", 0.1, "blue")
    console.print()
    write("things that you do", 0.11)
    time.sleep(0.5)
    write("are what remind me ", 0.11 ) 
    write("why i fell for you", 0.12) 
    console.print()
    write("and when we're apart", 0.12, "blue") 
    write("and i'm missing you", 0.12, "blue") 
    time.sleep(0.5)
    console.print()
    
    write("I close my eyes", 0.12)
    write("and all i see is you", 0.12) 
    console.print()
    time.sleep(0.5)
    write("and the small things you do 🤍", 0.1, "blue")  

    
    time.sleep(2)
    console.print()
    
    clear()

sing()\
    