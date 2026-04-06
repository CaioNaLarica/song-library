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
    write("Words like violence", 0.07,"red")
    time.sleep(0.1)
    write("Break the silence", 0.07,"red")
    time.sleep(0.1)
    write("Come crashing in", 0.07,"red" ) 
    time.sleep(0.1)
    write("Into my little world", 0.07,"red")
    console.print()
    time.sleep(0.3)
    write("Painful to me", 0.07)
    time.sleep(0.1)
    write("Pierce right through me", 0.07) 
    write("Can't you understand?", 0.07) 
    write("Oh, my little girl", 0.07)
    console.print()
    time.sleep(0.1)
    write("All I ever wanted", 0.07,"red") 
    time.sleep(0.2)
    write("All i ever needed is here in my arms", 0.1,"red") 
    time.sleep(1.5)
    write("Words are very unnecessary", 0.13,"red") 
    time.sleep(0.1)
    write("They can only do harm", 0.17,"red") 
  
    


  
    

    time.sleep(2)
    
    clear()

sing()
    