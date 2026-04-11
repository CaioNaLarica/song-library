
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
    write("Si supieran", 0.09,"yellow" )
    write("Que, por tu culpa, me la paso desvelado", 0.07)
    console.print()
    write("Que tú me llamas cuando se va ese pelado", 0.06, "yellow" )
    write("Que, en corto, yo me jalol", 0.05) 
    console.print()
    write("Mamita, tú me encantas, solo dime qué tranza", 0.05,"yellow")
    write("Que yo me voy pa' allá, me voy pa' allá", 0.06) 
    console.print()
    write("Me dices, Ven pa' acá, vente pa' acá ", 0.06, "yellow") 
    write("Y ahí te voy pa' allá, me voy pa' allá ", 0.06) 
    write("Bien desvelado---", 0.05) 

    
    

  
    

    time.sleep(2)
    
    clear()

sing()
    