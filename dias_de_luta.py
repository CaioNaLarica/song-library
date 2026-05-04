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
    write("Ô, minha gata, morada dos meus sonhos", 0.04,"blue")
    write("Todo dia, se eu pudesse, eu ia estar com você", 0.04)
    write("Eu já te via muito antes nos meus sonhos", 0.04, "blue" )
    time.sleep(0.2)
    write("Eu procurei a vida inteira por alguém como você", 0.04) 

    write("Por isso eu canto minha vida com orgulho", 0.04)
    console.print()
    write("Com melodia, alegria e barulho", 0.06, "blue")
    time.sleep(0.4) 
    write("Eu sou feliz e rodo pelo mundo", 0.05) 
    time.sleep(0.3)
    write("Sou correria, mas também sou vagabundo", 0.04, "blue") 

    console.print()
    time.sleep(0.5)
    write("Mas hoje dou valor de verdade", 0.04)
    time.sleep(0.2)

    write("Pra minha saúde e pra minha liberdade", 0.04, "blue")
    time.sleep(0.2)
    write("Que bom te encontrar nessa cidade", 0.04)
    time.sleep(0.5)
    write("Esse brilho intenso me lembra você", 0.04, "blue")

    console.print()
    time.sleep(1.5)
    write("História, nossas histórias", 0.04)

    time.sleep(2)
    
    clear()

sing()
