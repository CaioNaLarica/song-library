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
    write("Talvez você se vá antes que o sol levante, mas", 0.09)
    time.sleep(1.5)
    write("Eu vou te amar como um idiota ama", 0.09,"blue")
    console.print()
    write("Vou te pendurar num quadro bem do lado da minha cama", 0.07) 
    write("Eu espero enquanto você vive", 0.08)
    time.sleep(0.4)
    console.print()
    write("Mas não esquece que a gente existe", 0.07) 
    time.sleep(0.4)
    write("Eu vou te beijar como um idiota beija", 0.08, "blue")
    console.print()
    time.sleep(0.4)
    write("Vou me preparar pro dia em que você já não me queira", 0.06) 
    write("Mas enquanto você não se cansa", 0.08)
    time.sleep(0.5)
    write("Eu vou te amar como um idiota ama", 0.08, "blue") 

  
    

    time.sleep(2)
    
    clear()

sing()