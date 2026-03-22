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

    write("i still remember", 0.11, "blue")
    time.sleep(1.4)

    write("i was scared to take a breath", 0.09)

    write("didn't want you to move your 🎵", 0.07)
    write("how can we go", 0.11)

    console.print()

    write("back to being friends", 0.09, "blue")

    write("when we just shared a bed?", 0.1)

    time.sleep(2.3)

    write("how can you look", 0.12)
    write("at me and pretend", 0.11)

    console.print()

    write("i'm someone you've never met?", 0.09, "blue")

    time.sleep(2)

    console.print()

    clear()


sing()
