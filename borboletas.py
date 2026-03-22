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

    write("Dividido entre dois mundos", 0.04, "yellow")
    write("Sei que estou amando, mas ainda não sei quem", 0.07)
    console.print()

    write("Não sei dizer o que mudou", 0.09, "yellow")
    time.sleep(1.2)
    write("Mas nada está igual", 0.11)
    console.print()

    time.sleep(0.7)
    write("Numa noite estranha, a gente se estranha e fica mal", 0.1, "yellow")

    time.sleep(0.9)
    write("Você tenta provar", 0.12)
    console.print()

    time.sleep(1)
    write("Que tudo em nós morreu", 0.1, "yellow")

    time.sleep(0.5)
    write("Borboletas sempre voltam e o seu jardim sou eu 🌿", 0.11)

    time.sleep(2)

    clear()


sing()
