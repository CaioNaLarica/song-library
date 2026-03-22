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

    write("Everywhere I go, I know that I don't wanna be ", 0.06, "blue")
    write("Part of something,  won't ever need", 0.06)
    write("Your socialized", 0.07, "blue")

    console.print()

    write("romanticized life ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♬", 0.09)

    console.print()
    time.sleep(0.2)

    write("Floating on my low-key vibe", 0.07, "blue")
    write("Floating on my low-key vibe, vibe, vibe", 0.09)
    write("I don't need a night high", 0.08, "blue")
    write("I'm floating on...", 0.05)

    time.sleep(2)

    clear()


sing()
