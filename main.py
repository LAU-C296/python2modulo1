import argparse

# importando pacote
from personalizador.estilo import estilo_colorido, estilo_alerta
from personalizador.painel import painel_simples, painel_destaque
from personalizador.layout import layout_vertical, layout_duplo
from personalizador.progresso import progresso_simples, progresso_lento


# MAPA DE MÓDULOS E FUNÇÕES
MODULOS = {
    "estilo": {
        "1": estilo_colorido,
        "2": estilo_alerta,
        "colorido": estilo_colorido,
        "alerta": estilo_alerta
    },
    "painel": {
        "1": painel_simples,
        "2": painel_destaque,
        "simples": painel_simples,
        "destaque": painel_destaque
    },
    "layout": {
        "1": layout_vertical,
        "2": layout_duplo,
        "vertical": layout_vertical,
        "duplo": layout_duplo
    },
    "progresso": {
        "1": progresso_simples,
        "2": progresso_lento,
        "simples": progresso_simples,
        "lento": progresso_lento
    }
}


def main():
    parser = argparse.ArgumentParser(
        description="CLI do pacote Personalizador (Rich)"
    )

    # argumento obrigatório
    parser.add_argument(
        "texto",
        help="Texto ou caminho do arquivo"
    )

    # flag arquivo
    parser.add_argument(
        "-a", "--arquivo",
        action="store_true",
        help="Indica que o argumento é um arquivo"
    )

    # módulo
    parser.add_argument(
        "-m", "--modulo",
        required=True,
        help="Módulos disponíveis: estilo, painel, layout, progresso"
    )

    # função
    parser.add_argument(
        "-f", "--funcao",
        required=True,
        help="Funções disponíveis: depende do módulo (1, 2 ou nome)"
    )

    args = parser.parse_args()

    # pega módulo
    modulo = MODULOS.get(args.modulo)

    if not modulo:
        print("Módulo inválido!")
        return

    func = modulo.get(args.funcao)

    if not func:
        print("Função inválida!")
        return

    # executa função
    func(args.texto, args.arquivo)


if __name__ == "__main__":
    main()