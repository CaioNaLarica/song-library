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
    write("Tá vendo aí? Ela já tá falando", 0.07, "blue")
    write("Que tá com saudade e tá me procurando", 0.07)
    console.print()
    time.sleep(1)
    write("Daqui a pouco ela tá encostando", 0.07, "blue" ) 
    time.sleep(0.7)
    write("Sabe que sou louco e sem coração", 0.07) 
    write("Mas quando ela liga eu dou atenção", 0.07)
    console.print()
    time.sleep(1) 
    write("Eu mando logo a localização", 0.07, "blue") 
    time.sleep(0.3) 
    write("Hoje vai ter festa no colchão", 0.08) 
    console.print()
    time.sleep(1.5) 
    write("Ela roda a cidade inteira pra ficar comigo", 0.07, "blue") 
    write("Porque eu sou seu esquema preferido", 0.08, ) 
    write("Eu sou seu esquema preferido", 0.08, ) 


    time.sleep(2)
    
    clear()

sing()
    
