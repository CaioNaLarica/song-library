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
    write("I can see it in your eyes, that you wanna get out", 0.06,"blue")
    write("I can see it in your eyes, that you need it right now", 0.06,"blue")
    time.sleep(0.4)
    write("That you need it right now, that you wanna get out", 0.06)
    write("That you need it right now, that you wanna get out", 0.06)
    
    console.print()
 
    write("Yeah, I just wanna hear the sound, drive our Camaros out of town", 0.05 ) 
    write("Baby, we could leave right now, woah", 0.06) 
    write("Yeah", 0.07, "blue")
    time.sleep(0.6)
    write("I just wanna feel alive, baby, take your time", 0.06, "blue")
    console.print()
    time.sleep(0.1) 
    write("Smokin' on this loud, whoa", 0.06) 
    time.sleep(1)
    write("Girl, you know you make my cold heart warm with a touch", 0.06)
    console.print()
    write("One kiss, then we fuckin', I just can't get enough", 0.07, "blue") 
    write("Put it on me, that's the best part, baby, the trust", 0.07) 
    write("Trust me, I got nothin' for you other than love", 0.09, "blue") 
    
    
    console.print()
  
    

    time.sleep(2)
    
    clear()

sing()
    
