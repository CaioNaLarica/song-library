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
    write("No meu pensamento eu sei que vai ficar", 0.06)
    time.sleep(0.3)
    write("A todo momento, sei que vou lembrar", 0.08)
    write("Do brilho dos teus olhos", 0.08)
    console.print()
    time.sleep(2.3)
    write("Fecho os olhos, não consigo te esquecer", 0.07, "blue" ) 
    write("Tem alguém comigo, mas não é você", 0.08) 
    time.sleep(0.6)
    write("Tenho até medo de dormir, pra não lembrar", 0.07)
    console.print()
    time.sleep(0.7) 
    write("Daqueles olhos (aqueles olhos), aqueles olhos (inconfundíveis olhos)", 0.07, "blue") 
    write("Aqueles olhos, que refletem luz no meu coração", 0.15)
    console.print()
    write("Aqueles olhos (aqueles olhos), aqueles olhos (inconfundíveis olhos)", 0.09, "blue") 
    write("Aqueles olhos, que refletem luz no meu coração", 0.15) 
    
    console.print()
  
    

    time.sleep(2)
    
    clear()

sing()
    
