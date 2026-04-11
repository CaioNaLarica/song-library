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
    write("Às vezes no silêncio da noite", 0.1)
    time.sleep(4.2)
    write("Eu fico imaginando nós dois", 0.12, "yellow" )
    console.print()
    time.sleep(4.4)
    write("Eu fico ali sonhando acordado", 0.09 ) 
    time.sleep(2.5)
    write("Juntando", 0.06, "yellow" ) 
    time.sleep(1)
    console.print()
    write("O antes, o agora e o depois", 0.08) 
    time.sleep(5)
    write("Por que você me deixa tão solto?", 0.08, "yellow" )
    console.print()
    time.sleep(4) 
    write("Por que você não cola em mim?", 0.1) 
    time.sleep(4.5) 
    write("Tô me sentindo muito sozinho", 0.1, "yellow" ) 
    console.print()

    

    time.sleep(6)
    
    clear()

sing()