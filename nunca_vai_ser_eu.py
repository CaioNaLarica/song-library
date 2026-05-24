
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
    write("Seu olhar não nega quando a gente se encontra", 0.04,"yellow")
    write("Você fica tensa se entrega sem querer", 0.04)
    time.sleep(0.3) 
    write("Sempre não fala nada, mas eu sei que quer conversa", 0.04, "yellow" )
    write("Se quer saber então vou te dizer", 0.05) 
    console.print()
    time.sleep(0.2)
    write("Você tá beijando uma boca que não é sua", 0.04, "yellow")
    write("Tá abraçando um corpo que nunca foi seu", 0.06)
    time.sleep(0.2) 
    write("Ele tá te iludindo só pra te ter toda nua", 0.05, "yellow") 
    time.sleep(0.3)
    write("Mas a verdade é que você nunca me esqueceu", 0.06) 
    time.sleep(1.5) 
    console.print()
    write("Ele tá no meu lugar mas nunca vai ser eu", 0.05, "yellow") 
    write("Ele tá no meu lugar mas nunca vai ser eu", 0.05) 
    write("Ele tá no meu lugar mas nunca vai ser eu", 0.06, "yellow")
    time.sleep(0.6) 
    write("Porque seu coração é meu ", 0.06) 
    time.sleep(2)
    
    clear()

sing()
