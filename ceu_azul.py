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
    write("A gente nunca sabe quem são essas pessoas", 0.07)
    time.sleep(2)
    write("Eu só queria te lembrar", 0.11)
    console.print()
    time.sleep(2.7)
    write("Que aquele tempo, eu não podia fazer mais por nós", 0.08, "blue" ) 
    write("Eu estava errado e você não tem que me perdoar", 0.06) 
    time.sleep(1.9)
    write("Mas também quero te mostrar", 0.07)
    console.print()
    time.sleep(3.4) 
    write("Que existe um lado bom nessa história", 0.1, "blue") 
    write("Tudo o que ainda temos a compartilhar", 0.1) 
    console.print()
    write("E viver, e cantar", 0.14, "blue") 
  
    

    time.sleep(2)
    
    clear()

sing()
    