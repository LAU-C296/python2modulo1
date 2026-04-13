from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_simples(texto: str, isArquivo: bool):
    """Exibe um painel simples com o texto fornecido.
    
    Args:
        texto (str): O texto a ser exibido no painel.
        isArquivo (bool): Indica se o texto representa um arquivo ou não."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as file:
            texto = file.read()
    console.print(Panel(texto, title="Painel", style="cyan"))

def painel_destaque(texto: str, isArquivo: bool):
    """Exibe um painel de destaque com o texto fornecido.
    
    Args:
        texto (str): O texto a ser exibido no painel.
        isArquivo (bool): Indica se o texto representa um arquivo ou não."""
    if isArquivo:
        texto = open(texto, "r", encoding="utf-8").read()

    console.print(Panel(f"[bold yellow]{texto}[/bold yellow]", border_style="yellow"))
