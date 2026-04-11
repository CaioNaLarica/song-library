
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
    write("E eu te busco à meia-noite", 0.07)
    write("E, depois disso, a gente foge", 0.08)
    console.print()
    write("Pra algum lugar que ninguém vai nos encontrar", 0.08, "blue" ) 
    time.sleep(1.5)
    write("E, depois disso, a gente fode", 0.06) 
    write("Vamos fazer dessa a última noite", 0.07)
    console.print()
    write("Viver como se o amanhã não fosse chegar", 0.1, "blue") 
    write("Então vai", 0.1) 
    console.print()
    time.sleep(0.5)
    write("Tira a minha paz, tu senta demais", 0.12, "blue")
    time.sleep(0.7)
    write("Vai, faz de um jeito que só você faz", 0.12 )
    time.sleep(0.9)
    write("Tira a minha paz, tu senta demais", 0.12)
    time.sleep(0.8)
    write("Vai, faz de um jeito que só você faz", 0.12, "blue") 
     
  
    

    time.sleep(2)
    
    clear()

sing()