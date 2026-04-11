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
    write("Mas pode ficar sossegado", 0.07)
    time.sleep(0.5) 
    write("Tudo o que eu tô bebendo eu tô pagando", 0.08, "yellow") 
    write("Toca aí um João Mineiro e Marciano", 0.08) 
    console.print()
    time.sleep(1)
    write("Tô sofrendo, mas tá passando", 0.08, "yellow") 
    time.sleep(0.5)
    write("Mas pode ficar sossegado", 0.08) 
    write("Que eu não sou daquele tipo inconveniente", 0.07, "yellow") 
    write("Minha história é tão comum, igual de tanta gente", 0.07) 
    time.sleep(0.4)
    write("Ainda ontem chorei de saudade", 0.08, "yellow") 
    console.print()
    write("Quantas noites", 0.05) 
    write("E quantas garrafas preciso beber?", 0.08, "yellow") 
    time.sleep(1.5)
    write("Pra tirar do meu peito", 0.08) 
    write("Essa mágoa, pra te esquecer", 0.11, "yellow") 
    

    time.sleep(3)
    
    clear()

sing()