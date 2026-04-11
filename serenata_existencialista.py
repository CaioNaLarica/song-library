
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
    write("Estaremos enterrados em algum cemitério", 0.06,"yellow" )
    time.sleep(1.2)
    write("Sei que um dia eu vou morrer", 0.07)
    console.print()
    write("Saiba que isso também vale pra você", 0.05, "yellow" )
    write("Mas enquanto esse dia não vem", 0.06) 
    console.print()
    write("Quero passar todos os outros ao seu lado meu bem", 0.04,"yellow")
    write("Você precisa entender", 0.05) 
    console.print()
    write("Que a minha vida só se torna tolerável com você", 0.04, "yellow") 
    write("Tem que concordar, enquanto nossa hora não chega", 0.04) 
    write("A gente pode se beijar, pode aproveitar", 0.05) 
    
    write("Enquanto nossa hora não chega, a gente pode se beijar", 0.05) 
    time.sleep(1.5)
    write("Enquanto nossa hora não chega, a gente pode se beijar", 0.05) 
     

    

    time.sleep(2)
    
    clear()

sing()
    