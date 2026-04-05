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
    write("Violet, blue, green, red to keep me out", 0.09)
    write("I win", 0.07)
    write("There's things I wanna say to you", 0.07)
    console.print()
    time.sleep(0)
    write("But I'll just let you live", 0.07, "blue" ) 
    time.sleep(0.4)
    write("Like if you hold me without hurting me", 0.08) 
    write("You'll be the first who ever did", 0.08)
    time.sleep(0.4)
    write("There's things I wanna talk about", 0.08, "blue") 
    write("But better not to give", 0.08)
    time.sleep(0.5)
    console.print()
    write("But if you hold me without hurting me", 0.08, "blue") 
    write("You'll be the first who ever did", 0.08) 
    write("Ah, ah, ah, ah, ah, ah, Ah, ah, ah, ah", 0.2) 
    write("Hold me, love me, touch me, honey", 0.09,"blue") 
    write("Be the first who ever did", 0.09) 

    
    
    
    
    console.print()
  
    

    time.sleep(2)
    
    clear()

sing()
    