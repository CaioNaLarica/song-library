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
    write("Diga pra mim que é real", 0.11, "blue")
    time.sleep(1.5)
    write("Que eu te prometo meu melhor", 0.12)
    time.sleep(0.9)
    write("Fala pra mim o que eu quero ouvir", 0.09, "blue" )
    time.sleep(0.7)
    write("Que tu sentiu o que eu senti", 0.1) 
    time.sleep(0.9)
    console.print()
    write("Me diga agora, por favor (me diga agora, por favor)", 0.09, "blue")
    write("Que eu vou correndo te abraçar (que eu vou correndo-)", 0.08) 
    time.sleep(1)
    
  
    

    time.sleep(2)
    
    clear()

sing()