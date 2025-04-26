import tkinter as tk

def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(botao))

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora")

# Campo de entrada
entrada = tk.Entry(janela, width=16, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
entrada.grid(row=0, column=0, columnspan=4)

# Botões
botoes = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        comando = calcular
    else:
        comando = lambda t=texto: clicar(t)
    tk.Button(janela, text=texto, width=5, height=2, font=('Arial', 18), command=comando)\
        .grid(row=linha, column=coluna)

# Botão de limpar
tk.Button(janela, text='C', width=5, height=2, font=('Arial', 18), command=limpar)\
    .grid(row=5, column=0, columnspan=4, sticky='nsew')

# Executa a janela
janela.mainloop()
