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
    write("Véu e grinalda", 0.12, "magenta")
    write("Lua de mel", 0.13, "magenta")
    time.sleep(1)
    console.print()
    
    write("Chuva de arroz e tudo depois", 0.12)
    time.sleep(0.9)
    write("Dama de honra pega o buquê", 0.14)
    time.sleep(1.5)
    console.print()
    
    write("Ninguém mais feliz que eu e você...", 0.14, "magenta")
    time.sleep(3)

    clear()

sing()
