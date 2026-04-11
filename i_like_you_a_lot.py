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
    write("it's all a game to me", 0.08, "magenta") 
    console.print()
    time.sleep(1)
    write("anyway", 0.1)
    time.sleep(0.6)
    write("I like you a lot", 0.07)
    console.print()
    write("think I'II miss you forever", 0.08 ,"magenta") 
    console.print()
    write("like the stars miss the sun in the morning sky", 0.07) 
    write("late'r better than ever", 0.07 ) 
    time.sleep(0.2)
    write("even if you're gone", 0.07 )  
    write("I'm gonna drive 🎶", 0.07 )
    time.sleep(1)
    console.print()
    write("I got that sommertime", 0.08,"magenta" ) 
    write("summertime sadness", 0.08 ) 
    
    
    
    time.sleep(2)
    console.print()
    
    clear()

sing()\
    