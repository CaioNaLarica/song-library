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
    write("Walk, walk, fashion, baby", 0.05, "blue")
    write("Work it, move that bitch crazy", 0.05)
    console.print()
    write("Walk, walk, fashion, baby", 0.05, "blue" ) 
    write("Work it, move that bitch crazy", 0.05) 
    console.print()

    write("Walk, walk, fashion, baby", 0.05, "blue" ) 
    write("Work it, move that bitch crazy", 0.05) 
    write("Walk, walk, passion, baby", 0.05)
    console.print()
    write("Work it, I'm a free bitch, baby", 0.05, "blue") 
    time.sleep(0.4)
    write("I want your love and I want your revenge", 0.09) 
    console.print()
    write("I want your love, I don't wanna be friends", 0.07, "blue") 
    write("J'veux ton amour et je veux ta revanche", 0.08, "blue") 
    
    write("J'veux ton amour, I don't wanna be friends (oh-oh-oh-oh-oh-oh)", 0.09, "blue") 
    
  
    

    time.sleep(2)
    
    clear()

sing()
    