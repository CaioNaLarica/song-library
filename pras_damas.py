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
    write("Prometo que eu vou tentar te deixar menos nervosa", 0.04,"yellow" )
    write("E quando fizer merda, compro dois buquê de rosas", 0.05)
    console.print()
    write("E se ainda assim tiver nervosa, minha rainha inconstante", 0.04, "yellow" )
    time.sleep(0.1) 
    write("Session de massoterapia com incenso hidratante", 0.04) 
    console.print()
    time.sleep(0.1)
    write("Te prometo cada batida do meu coração", 0.05,"yellow")
    write("Prometo, teremos problemas, mas nunca sem solução", 0.05) 
    console.print()
    write("Promessas à parte, ficaremos sempre assim", 0.05, "yellow") 
    write("Eu gostando de você e você gostando de mim", 0.05) 
    

  
    

    time.sleep(2)
    
    clear()

sing()
    