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
    write("Seus olhos, meu clarão", 0.1,"green")
    time.sleep(1)
    write("Me guiam dentro da escuridão", 0.11)
    console.print()
    time.sleep(1)
    write("Seus pés me abrem o caminho", 0.1, "green" )
    time.sleep(0.8)
    write("Eu sigo e nunca me sinto só", 0.09)
    console.print()
    time.sleep(1.1)
    write("Você é assim", 0.1,"green")
    write("Um sonho pra mim", 0.09)
    console.print()
    write("Quero te encher de beijos 💚", 0.1, "green")
    

    time.sleep(2)
    
    clear()

sing()
    
