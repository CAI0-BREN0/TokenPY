import re
import tkinter as tk

# Definição dos tokens e expressões regulares
tokens = [
 ('NUMBER', r'\d+(\.\d+)?'),       # Números inteiros ou decimais
    ('MAIS', r'\+'),                  # Soma
    ('MENOS', r'\-'),                 # Subtração
    ('MULTIPLICACAO', r'\*'),         # Multiplicação
    ('DIVISAO', r'\/'),               # Divisão
    ('MOD', r'\%'),                   # Módulo
    ('POTE', r'\^'),                  # Potência
    ('RECEBE', r'\=='),               # Atribuição
    ('IGUAL', r'\='),                 # Igual
    ('PONTO', r'\.'),                 # Ponto
    ('VIRGULA', r'\,'),               # Vírgula
    ('LPAREN', r'\('),                # Parêntese esquerdo
    ('RPAREN', r'\)'),                # Parêntese direito
    ('LCOCHE', r'\]'),                # Colchete esquerdo
    ('RCOCHE', r'\['),                # Colchete direito
    ('LCHAVES', r'\}'),               # Chave esquerda
    ('RCHAVES', r'\{'),               # Chave direita
    ('AND', r'\&\&'),                 # Operador lógico AND
    ('OR', r'\|\|'),                  # Operador lógico OR
    ('NOT', r'\!'),                   # Operador lógico NOT
    ('XOR', r'\^'),                   # Operador lógico XOR
    ('BITWISE_AND', r'\&'),           # Operador bitwise AND
    ('BITWISE_OR', r'\|'),            # Operador bitwise OR
    ('BITWISE_NOT', r'\~'),           # Operador bitwise NOT
    ('BITWISE_XOR', r'\^'),           # Operador bitwise XOR
    ('SHIFT_LEFT', r'\<\<'),          # Operador de deslocamento à esquerda
    ('SHIFT_RIGHT', r'\>\>'),         # Operador de deslocamento à direita
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Identificador
    ('SPACE', r'\s+'),                # Espaço
    ('NEWLINE', r'\n'),      # Identificador
]

def tokenize(input_string):
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)
    for match in re.finditer(token_regex, input_string):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'SPACE' and token_type != 'NEWLINE':
            yield token_type, token_value

def processar():
    input_string = entrada.get()
    tokens_listbox.delete(0, tk.END)
    for token in tokenize(input_string):
        tokens_listbox.insert(tk.END, token)

# Variável para controlar o tema atual
dark_mode = False

def toggle_dark_mode():
    global dark_mode
    if not dark_mode:
        root.tk_setPalette(background='black', foreground='white')
        dark_mode_button.config(text="Modo Claro")
        dark_mode = True
    else:
        root.tk_setPalette(background='white', foreground='black')  # Use light theme
        dark_mode_button.config(text="Modo Escuro")
        dark_mode = False
def show_tokens():
    tokens_listbox.delete(0, tk.END)
    for token in tokens:
        tokens_listbox.insert(tk.END, token)

# Criando a janela principal
root = tk.Tk()
root.title("Tokenizador de Expressões Matemáticas")
root.geometry("900x400")  # Define tamanho da janela

# Criando os widgets
entrada_label = tk.Label(root, text="Expressão Matemática:")
entrada_label.grid(row=0, column=0)

entrada = tk.Entry(root, width=60)
entrada.grid(row=0, column=1)

processar_button = tk.Button(root, text="Processar", command=processar)
processar_button.grid(row=0, column=2)

dark_mode_button = tk.Button(root, text="Modo Escuro", command=toggle_dark_mode)
dark_mode_button.grid(row=0, column=3)

tokens_button = tk.Button(root, text="Mostrar Tokens", command=show_tokens)
tokens_button.grid(row=0, column=4)

tokens_label = tk.Label(root, text="Tokens:")
tokens_label.grid(row=1, column=0, sticky=tk.W)

tokens_listbox = tk.Listbox(root, width=90, height=15)
tokens_listbox.grid(row=4, column=0, columnspan=10, padx=20, pady=20)

# Rodando o loop principal
root.mainloop()
