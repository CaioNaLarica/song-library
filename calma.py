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

    write("Não chore nunca mais, amor", 0.09, "yellow")
    write("ooÖOOOOOOOHHHH", 0.07)

    console.print()
    time.sleep(1.02)

    write("Calma, a sua insegurança não te leva a nada", 0.08, "yellow")
    write("Eu quero ser seu homem, te fazer amada", 0.09)

    console.print()

    write("Amar, amar você até você se amar e me amar", 0.09, "yellow")

    time.sleep(1.1)

    write("Calma, a sua insegurança não te leva a nada", 0.1)

    console.print()
    time.sleep(0.12)

    write("Eu quero ser seu homem, te fazer amada", 0.08, "yellow")

    time.sleep(0.4)

    write("Amar, amar você até você se amar e me amar", 0.09)

    time.sleep(1.7)

    console.print()

    write("Calma!", 0.14, "yellow")

    time.sleep(2)

    clear()


sing()
