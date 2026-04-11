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
    write("Every day and every night", 0.11)
    time.sleep(2)
    write("I always dream that you are by my side", 0.11)
    console.print()
    time.sleep(2)
    write("Oh, baby, every day and every night", 0.11, "blue" ) 
    time.sleep(1.4)
    write("Well, I said everything's gonna be alright", 0.1) 
    time.sleep(2)
    write("And I'll fly with you 🎶", 0.1)
    console.print()
    time.sleep(3.7) 
    write("I'll fly with you🎶", 0.1, "blue") 
    time.sleep(4.5) 
    write("I'll fly with you🎶", 0.1) 
    time.sleep(7) 
    console.print()
   
  
    

    time.sleep(2)
    
    clear()

sing()