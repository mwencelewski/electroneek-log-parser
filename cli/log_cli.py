from rich import print
from rich.console import Console
from rich.prompt import Prompt

console = Console()


if __name__ == "__main__":
    style = "bold white on blue"
    console.print("ElectroNeek Log Parser", style=style, justify="center")
    name = Prompt.ask("Enter your name", choices = ["Bot Runner", "Orchestrator"], default="Mauro")
