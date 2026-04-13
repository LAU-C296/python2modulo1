from rich.progress import Progress
import time

def progresso_simples(texto: str, isArquivo: bool):
    """'Exibe um progresso simples com o texto fornecido."""
    if isArquivo:
        texto = open(texto, "r", encoding="utf-8").read()

    with Progress() as progress:
        task = progress.add_task(f"[cyan]{texto}", total=100)

        while not progress.finished:
            progress.update(task, advance=5)
            time.sleep(0.03)


def progresso_lento(texto: str, isArquivo: bool):
    """Exibe um progresso lento com o texto fornecido."""
    if isArquivo:
        texto = open(texto, "r", encoding="utf-8").read()

    with Progress() as progress:
        task = progress.add_task(f"[green]Processando: {texto}", total=50)

        for _ in range(50):
            time.sleep(0.05)
            progress.update(task, advance=1)