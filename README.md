# Personalizador Rich

Projeto desenvolvido como exercício prático de Python, explorando **ambientes virtuais**, **pacotes e módulos**, **docstrings**, **argparse** e **match-case**, com a biblioteca de formatação de terminal [Rich](https://github.com/Textualize/rich).

---

## Estrutura do Projeto

```
projeto_rich/
├── personalizador/          # Pacote principal
│   ├── __init__.py          # Inicialização e mapeamentos do pacote
│   ├── layout.py            # Módulo de layouts e colunas (id=0)
│   ├── painel.py            # Módulo de painéis estilizados (id=1)
│   ├── progresso.py         # Módulo de progresso e spinners (id=2)
│   └── estilo.py            # Módulo de estilos tipográficos e tabelas (id=3)
├── docs/                    # Documentação HTML gerada pelo pydoc
│   ├── personalizador.html
│   ├── personalizador_layout.html
│   ├── personalizador_painel.html
│   ├── personalizador_progresso.html
│   └── personalizador_estilo.html
├── main.py                  # Interface de linha de comando (argparse)
├── gerar_docs.py            # Script para gerar a documentação HTML
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo
```

---

## Configuração do Ambiente

### 1. Criar o ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

**Linux / macOS:**
```bash
source venv/bin/activate
```

**Windows (CMD):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

Quando ativado, o terminal exibirá `(venv)` no início da linha.

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## Como Usar

### Sintaxe geral

```bash
python main.py <texto> [opções]
```

### Argumentos

| Argumento          | Tipo       | Descrição                                                        |
|--------------------|------------|------------------------------------------------------------------|
| `texto`            | Obrigatório | Texto a exibir ou caminho para um arquivo (use `-a` para arquivo) |
| `-a`, `--arquivo`  | Flag        | Indica que o argumento é o caminho de um arquivo de texto        |
| `-m`, `--modulo`   | Opcional    | Módulo a usar (nome ou id). Padrão: `painel`                     |
| `-f`, `--funcao`   | Opcional    | Função a executar (nome ou id). Padrão: `0`                      |

### Módulos e funções disponíveis

| ID | Módulo      | Funções disponíveis                                    |
|----|-------------|--------------------------------------------------------|
| 0  | `layout`    | `exibir_colunas` (0), `exibir_dividido` (1)            |
| 1  | `painel`    | `exibir_painel_simples` (0), `exibir_painel_duplo` (1) |
| 2  | `progresso` | `exibir_com_progresso` (0), `exibir_com_spinner` (1)   |
| 3  | `estilo`    | `exibir_estilizado` (0), `exibir_tabela_palavras` (1)  |

---

## Exemplos de Uso

```bash
# Texto simples com o módulo padrão (painel)
python main.py "Python é incrível!"

# Escolhendo módulo e função pelo nome
python main.py "Olá, mundo!" -m layout -f exibir_colunas

# Escolhendo módulo e função pelo id
python main.py "Olá, mundo!" -m 2 -f 1

# Lendo de um arquivo
python main.py conteudo.txt -a -m estilo -f exibir_tabela_palavras

# Arquivo com módulo e função por id
python main.py conteudo.txt -a -m 0 -f 1

# Exibir ajuda
python main.py --help
```

---

## O Pacote `personalizador`

### `layout` — Layouts e Colunas

Usa `Layout` e `Columns` da Rich para organizar o texto visualmente.

- **`exibir_colunas(texto, isArquivo)`** — Divide o texto por parágrafos e exibe cada um em uma coluna colorida lado a lado.
- **`exibir_dividido(texto, isArquivo)`** — Exibe o texto em um layout estruturado com cabeçalho, corpo e rodapé com estatísticas.

### `painel` — Painéis Estilizados

Usa `Panel`, `Align` e `Padding` da Rich para criar painéis com borda.

- **`exibir_painel_simples(texto, isArquivo)`** — Exibe o texto centralizado dentro de um painel com borda magenta.
- **`exibir_painel_duplo(texto, isArquivo)`** — Exibe o texto em dois painéis: um com o conteúdo e outro com estatísticas (caracteres, palavras, linhas).

### `progresso` — Progresso e Spinners

Usa `Progress`, `Live` e `Spinner` da Rich para animações de carregamento.

- **`exibir_com_progresso(texto, isArquivo)`** — Processa o texto linha a linha com uma barra de progresso animada e, ao final, exibe o texto completo.
- **`exibir_com_spinner(texto, isArquivo)`** — Exibe um spinner com mensagens de status antes de mostrar o texto em um painel.

### `estilo` — Estilos Tipográficos e Tabelas

Usa `Text`, `Style` e `Table` da Rich para formatação avançada.

- **`exibir_estilizado(texto, isArquivo)`** — Aplica uma cor diferente a cada palavra do texto de forma cíclica.
- **`exibir_tabela_palavras(texto, isArquivo)`** — Exibe cada palavra do texto em uma linha de tabela com informações de índice, comprimento e capitalização.

---

## Documentação (pydoc)

A documentação HTML foi gerada com `pydoc` e está disponível na pasta `docs/`.

Para **abrir** a documentação:

```bash
# Linux/macOS
open docs/personalizador.html

# Windows
start docs/personalizador.html
```

Para **regenerar** a documentação (com o ambiente virtual ativado):

```bash
python gerar_docs.py
```

---

## Conceitos Aplicados

### Ambiente Virtual
O projeto usa `venv` para isolar as dependências. Apenas `rich` é necessário como dependência externa, declarada em `requirements.txt`.

### Pacotes e Módulos
O código está organizado no pacote `personalizador/`, com quatro módulos (`layout`, `painel`, `progresso`, `estilo`). O arquivo `__init__.py` expõe mapeamentos de nomes e ids usados pelo `main.py`.

### Docstrings
Todos os módulos, funções e o próprio `main.py` possuem docstrings no estilo **Google Style**, documentando parâmetros (`Args`), retornos (`Returns`), exceções (`Raises`) e exemplos de uso (`Example`).

### Argparse
O `main.py` usa `argparse` para criar uma interface de linha de comando completa com:
- Argumento posicional obrigatório (`texto`)
- Flag booleana `-a / --arquivo`
- Opções com valor `-m / --modulo` e `-f / --funcao` (aceitam nome ou id)
- Mensagem de `--help` automática e um epilog com todas as opções listadas

### Match-Case
Usado em `main.py` na função `resolver_modulo()` para mapear o valor do argumento `-m` (nome ou id numérico) para o módulo correspondente, substituindo uma cadeia de `if/elif` por um `match-case` mais legível.

---

## Requisitos

- Python **3.10+** (necessário para o `match-case`)
- rich **>= 13.0.0**

---

## Desativar o Ambiente Virtual

Quando terminar de trabalhar no projeto:

```bash
deactivate
```
