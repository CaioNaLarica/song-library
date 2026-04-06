


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
    write("You could bet that", 0.03, "blue" )
    write("Never gotta sweat that", 0.03)
    console.print()
    write("You could be the lover",  0.03, "blue" ) 
    write("I'll be the fighter, baby",  0.04) 
    write("If I'm the blunt",  0.04, "blue" )
    console.print()
    write("You could be the lighter, baby", 0.04) 
    write("Fire it up!", 0.04, "blue" ) 
    console.print()
    write("Writer, baby",  0.03) 
    write("You could be the quote",  0.04, "blue") 
    write("If I'm the lyric, baby",  0.05) 
    write("You could be the note",  0.05, "blue") 
    write("Saint, I'm a sinner",  0.05) 
    write("Prize, I'm a winner",  0.06, "blue") 
    write("And it's you",  0.05) 
    write("What can I do to deserve that",  0.04, "blue") 
    write("Paper, baby, I'll be the pen",  0.05) 
    
    write("Say that I'm the one",  0.05, "blue") 
    write("'Cause you are ten", 0.05) 
    write("Real and not pretend!", 0.05, "blue") 
    write("Even when the sky comes fallin'",  0.06) 
    time.sleep(0.3)
    write("Even when the Sun don't shine",  0.06, "blue") 
    write("We can do it, baby, simple and plain",  0.03) 
    time.sleep(0.6)

    write("This love is a sure thing",  0.06, "blue") 
    
    
    
    
    
    
    
    
    
    
  
    

    time.sleep(2)
    
    clear()

sing()
    