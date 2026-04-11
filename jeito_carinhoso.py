
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
    write("Quero te ver pra me entregar", 0.11, "yellow")
    time.sleep(4)
    write("Como eu quero", 0.11)
    console.print()
    time.sleep(0.3)
    write("De novo um beijo seu muito gostoso", 0.06, "yellow" ) 
    write("Do jeito que cê faz é carinhoso", 0.06) 
    write("Por isso eu quero suas mãos em mim", 0.06, "yellow")
    console.print()
    write("Como eu quero", 0.11) 
    time.sleep(0.3)
    write("O cheiro de amor que vem chegando", 0.06, "yellow")
    time.sleep(0.3)
    write("Trazendo o seu corpo só pra mim", 0.1) 
  
    

    time.sleep(3)
    
    clear()

sing()