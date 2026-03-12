import time
import sys
import os
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")


banner = pyfiglet.figlet_format("Undressed")

console.print(  
    Panel.fit(
        Align.center(banner),
        style="bold magenta"
    )
)


with Progress(
    SpinnerColumn(),
    TextColumn("[purple]Loading music..."),
    BarColumn(),
    TextColumn("{task.percentage:>3.0f}%"),
) as progress:

    task = progress.add_task("", total=100)

    for _ in range(100):
        time.sleep(0.02)
        progress.update(task, advance=1)

clear()


def write(text, speed, cor="yellow"):
    linha = ""

    for lyrics in text:
        linha += lyrics
        console.print(f"[{cor}]{linha}[/]", end="\r")
        time.sleep(speed)

    console.print(f"[bold {cor}]{text}[/]")
    time.sleep(0.6)


def sing():

    console.print()

    write("I don't wanna get undressed", 0.13)
    write("For a new person all over again", 0.11)
    write("I don't wanna kiss someone else's neck", 0.1)
    write("And have to pretend it's yours instead", 0.09)

    write("\n♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♬", 0.02, "magenta")
    clear()

    console.print()

    write("And I don't wanna learn another scent", 0.09)
    write("I don't want the children of another man", 0.06)
    write("To have the eyes of the girl that I won't forget", 0.08)

    write("\n♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♬", 0.10, "magenta")
    clear()
    write("I won't forget", 0.13)
    write("\n♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♪ ♫ ♬ ♪ ♫ ♬ ♪ ♫ ♬", 0.11, "magenta")


sing()