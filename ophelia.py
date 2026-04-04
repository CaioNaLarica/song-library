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
    write("Saved my heart from the fate of", 0.05)
    write("Opheliaaaaaaaaaaa", 0.08,"magenta")
    time.sleep(1.3)
    write("Keep it one hundred", 0.06)
    console.print()
 
    write("On the land, the sea, the sky", 0.06, "mangeta" ) 
    write("Pledge allegiance to your hands", 0.06) 
    write("Your team, your vibes", 0.05)
    console.print()
    time.sleep(0.1) 
    write("Don't care where the hell you been", 0.05, "magenta") 
    write("'Cause now you're mine", 0.04)
    console.print()
    write("It's 'bout to be the sleepless night", 0.05, "magenta") 
    write("You've been dreaming of", 0.05) 
    write("The fate of Ophelia", 0.1) 
    
    
    console.print()
  
    

    time.sleep(2)
    
    clear()

sing()
    
