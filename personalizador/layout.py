"""Módulo de layout para exibir textos em diferentes formatos usando a biblioteca Rich.
Este módulo define funções para criar layouts verticais e duplos, permitindo a exibição de"""
from rich.console import Console
from rich.layout import Layout

console = Console()

def layout_vertical(texto: str, isArquivo: bool):
    """'Exibe um layout vertical com o texto fornecido."""
    if isArquivo:
        texto = open(texto, "r", encoding="utf-8").read()

    layout = Layout()
    layout.split_column(
        Layout("[bold cyan]TOP[/bold cyan]"),
        Layout(texto),
        Layout("[bold magenta]BOTTOM[/bold magenta]")
    )

    console.print(layout)


def layout_duplo(texto: str, isArquivo: bool):
    """Exibe um layout duplo com o texto fornecido."""
    if isArquivo:
        texto = open(texto, "r", encoding="utf-8").read()

    layout = Layout()
    layout.split_row(
        Layout(f"[green]ESQUERDA:\n{texto}[/green]"),
        Layout(f"[blue]DIREITA:\n{texto}[/blue]")
    )

    console.print(layout)