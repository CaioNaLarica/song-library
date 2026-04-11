
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
    write("Era ele virar e você me olhava pra gente combinar", 0.05)
    write("Um sinal disfarçado com o jeito safado", 0.04)
    write("Gostoso de me olhar", 0.07, "blue" )
    time.sleep(1.1)
    console.print()
    write("Vai no banheiro pra gente se beijar", 0.07) 
    write("Bem lá no escurinho pra ninguém desconfiar", 0.07)
    console.print()
    time.sleep(0.5)
    write("Cara de santa mais não me engana não", 0.06, "blue") 
    write("É hoje que eu te pego", 0.06) 
    write("E você não escapa não", 0.07, "blue") 
  
    

    time.sleep(2)
    
    clear()

sing()