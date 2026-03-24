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
    write("cê disse que queria espaço, eu te dei uma mansão", 0.03)

    write("acho que eu entendi errado, agi na emoção", 0.05)

    write("Eu te pedi: Me dá mão, será que tu levou a mal?", 0.04)
    write("Demos um salto tão alto, que acho que foi mortal", 0.03)
    console.print()
    write("A gente era um casal, um casal sensacional", 0.03,"red")

    write("Cê era minha senhorita, linda, e eu nem sou Cabal", 0.04,"red")
    write("Descobri sua geografia que nem Pedro Cabral", 0.04,"red")

    write("Nós tava sintonizado, mas mudou de canal", 0.05,"red")





    write("e", 0.02)

    clear()

sing()