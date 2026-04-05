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
    write("Em minhas mãos agora", 0.04,"yellow" )
    write("Tá cada parte dessa nossa história", 0.07)
    console.print()
    write("E eu não sei se eu rasgo ou jogo fora", 0.09, "yellow" )
    time.sleep(1.2) 
    write("E o que é que eu faço agora", 0.11) 
    console.print()
    time.sleep(0.7)
    write("Cometi a loucura de nossas fotos rasgar", 0.1,"yellow")
    time.sleep(0.9)
    write("E uma por uma eu vou ter que colar", 0.12) 
    console.print()
    time.sleep(1)
    write("Mas foi na hora da raiva", 0.1, "yellow") 
    time.sleep(0.5)
    write("Na hora na hora da raiva", 0.11) 
    

  
    

    time.sleep(2)
    
    clear()

sing()
    