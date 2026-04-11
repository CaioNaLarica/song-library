
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
    write("Eu não quero mais", 0.05)
    write("Essa vida de farra", 0.04)
    console.print()
    time.sleep(0.8)
    write("Quando é que cê vai perceber que eu lutei pra te ter?", 0.04, "blue" ) 
    write("Te quero ao meu lado, eu sei", 0.03) 
    write("que a minha fama não é boa", 0.03)
    write("E o povo me chama de beijo safado, mas eu", 0.04, "blue") 
    time.sleep(1.2)
    write("não quero mais", 0.05) 
    console.print()
    write("Essa vida de farra", 0.05, "blue") 
    time.sleep(0.7)
    write("Tô precisando de dengo, não vê?", 0.06, "blue") 
    time.sleep(0.7)
    write("Tô nem aí pra rolê", 0.07, "blue") 
    write("Tô nem aí pra role", 0.07, "blue") 
    
  
    

    time.sleep(2)
    
    clear()

sing()