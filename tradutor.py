import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator

def traduzir():
    texto = entrada.get()
    direcao = idioma_var.get()

    if not texto:
        messagebox.showwarning("Aviso", "Digite uma palavra ou frase!")
        return

    if direcao == "PT → EN":
        origem = "pt"
        destino = "en"
    else:
        origem = "en"
        destino = "pt"

    try:
        traducao = GoogleTranslator(source=origem, target=destino).translate(texto)
        resultado_var.set(traducao)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro na tradução:\n{str(e)}")

# Janela principal
janela = tk.Tk()
janela.title("Tradutor Simples")
janela.geometry("400x250")
janela.resizable(False, False)

# Entrada
tk.Label(janela, text="Digite a palavra/frase:").pack(pady=5)
entrada = tk.Entry(janela, width=40)
entrada.pack(pady=5)

# Seleção de idioma
idioma_var = tk.StringVar(value="PT → EN")
tk.OptionMenu(janela, idioma_var, "PT → EN", "EN → PT").pack(pady=5)

# Botão
tk.Button(janela, text="Traduzir", command=traduzir).pack(pady=10)

# Resultado
resultado_var = tk.StringVar()
tk.Label(janela, textvariable=resultado_var, font=("Arial", 12, "bold")).pack(pady=10)

# Loop da interface
janela.mainloop()
