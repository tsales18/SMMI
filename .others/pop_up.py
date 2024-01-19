import tkinter as tk
from tkinter import messagebox

def exibir_popup():
    messagebox.showinfo("Título do Pop-up", "Esta é uma mensagem de pop-up!")

# Criar a janela principal
root = tk.Tk()
root.title("Janela Principal")

# Botão que exibe o pop-up
botao_popup = tk.Button(root, text="Exibir Pop-up", command=exibir_popup)
botao_popup.pack(pady=20)

# Iniciar o loop principal da GUI
root.mainloop()