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
    write("Se lembre que eu há muito tempo te amo", 0.07)
    time.sleep(0.4)
    write("Te amo, te amo", 0.07,"yellow")
    console.print()
    time.sleep(1.1)
    write("Quero fazer você feliz", 0.1) 
    time.sleep(1.6)
    write("Vamos pegar o primeiro avião", 0.1,"yellow")
    time.sleep(0.5)
    console.print()
    write("Com destino à felicidade", 0.09) 
    time.sleep(0.6)
    write("A felicidade pra mim é você", 0.11, "yellow")
    console.print()
    time.sleep(1.7)
    write("Pense em mim, chore por mim", 0.1) 
    write("Liga pra mim, não, não liga pra ele", 0.09,"yellow")
    time.sleep(0.5)
    write("Pense em mim, chore por mim", 0.09) 
    write("Liga pra mim, não, não liga pra ele", 0.09, "yellow") 
    time.sleep(0.5)
    write("Pra ele! Não chore por ele", 0.11)
    


  
    

    time.sleep(2)
    
    clear()

sing()
    
