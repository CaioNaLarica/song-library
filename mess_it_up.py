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
    write("'Cause every time I get too close, I just go mess it up", 0.07)
    time.sleep(0.2)
    write("I keep thinking maybe if you let me back in", 0.05)
    time.sleep(0.6)
    write("We can make it better, breaking every habit", 0.06)
    time.sleep(0.1)
    write("Pull myself together, you could watch it happen", 0.05)
    time.sleep(0.5)
    console.print()
    write("Let it happen", 0.09,"red")
    write("Let it happen", 0.09,"red")

    console.print()
    time.sleep(0.8)
    write("I keep thinking maybe if you let me back in", 0.05)
    time.sleep(0.5)
    write("We can make it better, breaking every habit", 0.05)
    time.sleep(0.5)
    write("Pull myself together, you could watch it happen", 0.06)
    time.sleep(0.8)
    console.print()
    write("Let it happen", 0.08,"red")
    write("Let it happen", 0.08,"red")


    clear()

sing()