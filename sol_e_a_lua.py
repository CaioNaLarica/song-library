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

    write("E vinte e quatro horas se passaram", 0.04)
    write("e outra vez", 0.05)
    write("o sol se pôs, a lua nasceu", 0.05)
    write("e de novo", 0.01)
    write("e de novo", 0.01)
    write("e de novo", 0.01)

    console.print()

    write("O sol pediu a lua em casamento", 0.19, "yellow")
    write("e a lua, disse:", 0.23, "yellow")
    write("NÃO SEI...", 0.01, "yellow")
    write("NÃO SEI...", 0.01, "yellow")
    write("NÃO SEI...", 0.01, "yellow")
    write("me dá um tempo", 0.07, "yellow")

    console.print()

    write("o sol congelou seu coração", 0.13)

    time.sleep(2)

    console.print()

    clear()


sing()
