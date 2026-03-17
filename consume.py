import time
import os
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()
print("\n\n\n")
banner = pyfiglet.figlet_format("Consume")
console.print(Panel(Align.center(banner), style="bold red on black", padding=(1, 2)))

with Progress(
    SpinnerColumn(style="red"),
    TextColumn("[white]Let the music begin..."),
    BarColumn(style="white"),
    TextColumn("{task.percentage:>3.0f}%", style="bold red"),
) as progress:

    task = progress.add_task("", total=100)

    for _ in range(100):
        time.sleep(0.02)
        progress.update(task, advance=1)

clear()

def write(text, speed, cor="white"):
    linha = ""

    for lyrics in text:
        linha += lyrics
        console.print(f"[{cor}]{linha}[/]", end="\r")
        time.sleep(speed)

    console.print(f"[bold {cor}]{text}[/]")
    time.sleep(0.6)

def sing():
    console.print()

    write("And you can take my flesh", 0.05)
    write("If you want girl", 0.03)
    write("But baby, don't abuse it", 0.08)
    write("\n♪ ♫ ♬ ♪ ♫ ♬ ♪ ♬ ", 0.04, "red")
    clear()
    print("")
    write("these voices in my head screaming, Run, now", 0.08)

    console.print()

    write("I'm praying that they're human", 0.05)

    console.print()
    write("Rollin', rollin", 0.11)

sing()
