"""Personalizador de estilo para o terminal usando a biblioteca Rich.
Este módulo define a classe `PersonalizadorEstilo` que permite personalizar o estilo do terminal, incluindo cores, fontes e outros elementos visuais."""
from rich import print 


def estilo_colorido(texto: str, isArquivo: bool):
    """Aplica um estilo colorido ao texto."""

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()

    print(f"[bold green]{texto}[/bold green]")

def estilo_alerta (texto: str, isArquivo: bool):
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    print(f"[bold red on white]⚠ {texto}[/bold red on white]")

