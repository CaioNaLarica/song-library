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
    write("Como se o silêncio dissesse tudo", 0.07, "blue")
    write("Um sentimento bom que me leva pra outro mundo", 0.07)
    write("A vontade de te ver já é maior que tudo", 0.08, "blue" ) 
    write("Não existem distâncias no meu novo mundo", 0.08) 
    time.sleep(0.2)
    console.print()
    write("Tipo coisas da sétima arte", 0.08, "blue")
    time.sleep(0.7)
    write("Aconteceu sem que eu imaginasse", 0.08) 
    time.sleep(0.9)
    write("Sonho de consumo cantar na sua festa", 0.08) 
    write("Vem dançar comigo, aproveita e me sequestra", 0.09, "blue") 
    write("Amor vagabundo, intenso ou muita pressa", 0.1) 
    write("Não sei como termina, mas sei como começa", 0.08, "blue") 
    
  
    

    time.sleep(2)
    
    clear()

sing()