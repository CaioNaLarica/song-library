import time
import os
from rich.console import Console
from rich.live import Live
from rich.panel import Panel

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

def loading_screen():
    mensagens = [
        "Eterno Ganley",
        "Obrigado por tudo",
        "Você sempre será nosso futuro Olympia 🥇",
    ]

    for msg in mensagens:
        clear()

        painel = Panel(
            f"""
[bold white]EM MEMÓRIA DE GABRIEL GANLEY[/]

[white]{msg}[/]
            """,
            border_style="blue",
            width=70
        )

        # só desce no eixo vertical
        print("\n" * 6)

        # painel realmente na esquerda
        console.print(painel)

        time.sleep(1)

    clear()

    painel_final = Panel(
        """
[bold white]ATÉ O ÚLTIMO TREINO[/]
        """,
        border_style="blue",
        width=70
    )

    print("\n" * 6)

    # esquerda real
    console.print(painel_final)

    time.sleep(3)
    clear()

def sing():
    clear()

    write("JANE!", 0.05)
    time.sleep(0.5)

    console.print()

    write("you're early", 0.08, "blue")
    time.sleep(0.5)

    write("your life's work is dirtied by the fools", 0.07)
    time.sleep(0.1)

    write("who adore you", 0.07)
    time.sleep(1.5)

    write("only to find", 0.1, "blue")
    write("only to find you out", 0.08)

    console.print()
    time.sleep(0.5)

    write("they saw you ", 0.08, "blue")
    write("dressing in the backroom now they'll pay! ", 0.08)
    write("what they owe you", 0.07, "blue")

    time.sleep(1)

    write("it's only small chance", 0.07)
    write("red on the green green GRASS", 0.07, "blue")

    time.sleep(2)

    clear()

loading_screen()
sing()
