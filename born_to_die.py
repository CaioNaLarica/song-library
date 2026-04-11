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
    write("I feel so alone on the Friday nights", 0.08, "magenta") 
    console.print()
    time.sleep(0.6)
    write("Can you make it feel like home if I tell you you're mine?", 0.1)
    time.sleep(0.1)
    write("It's like I told you, honey (louder)", 0.07)
    console.print()
    write("Don't make me sad, don't make me cry", 0.09 ) 
    console.print()
    write("Sometimes love is not enough", 0.08,"magenta") 
    write("And the road gets tough, I don't know why", 0.07 ) 
    write("Keep making me laugh", 0.08 )  
    write("Let's go get high", 0.07 )
    time.sleep(0.5)
    write("The road is long, we carry on", 0.08 ) 
    write("Try to have fun in the meantime", 0.09 ) 
    
    
    
    time.sleep(2)
    console.print()
    
    clear()

sing()\
    