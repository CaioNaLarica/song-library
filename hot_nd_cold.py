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
    write("You change your mind like a girl changes clothes", 0.1, "magenta") 
    console.print()
    time.sleep(1)
    write("Yeah, you PMS", 0.12)
    time.sleep(0.4)
    write("like a bitch", 0.12)
    
    time.sleep(0.7)
    write("I would know", 0.1)
    time.sleep(0.5)
    write("And you", 0.09)
    write("Ooverthink", 0.1)
    write("always speak", 0.09)
    time.sleep(0.2)
    write("cryptically", 0.09)
    time.sleep(0.5)
    write("I should know ", 0.09 ) 
    write("that you're no good for me", 0.09 ) 
    console.print()
    time.sleep(2.8)
    write("'Cause you're hot, then you're cold", 0.04,"magenta") 
    write("You're yes, then you're no", 0.05,"magenta") 
    write("You're in, then you're out", 0.05,"magenta") 
    write("You're up, then you're down", 0.05,"magenta") 
    write("You're wrong when it's right", 0.04,"magenta") 
    write("It's black, and it's white", 0.04,"magenta") 
    write("We fight, we break up", 0.04,"magenta") 
    write("We kiss, we make up", 0.05,"magenta") 
    
    
    time.sleep(2)
    console.print()
    
    clear()

sing()\
    