# sobre.py

import tkinter as tk
from tkinter import ttk, messagebox
from configBanco import BancoDados

class TelaSobre:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sobre")
        
        # Define o tamanho da janela
        largura = 800
        altura = 150

        # Obtém as dimensões da tela
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        # Calcula as coordenadas para centralizar a janela na tela
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2

        # Define a geometria da janela para centralizá-la
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

        # Cria um frame para conter os elementos
        frame = ttk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        # Label de sobre, estatica com as informações que setar no codigo.
        sobre_label = ttk.Label(frame, text="Está aplicação foi desenvolvida pelo Augusto, Gabriel e Vinicius, com o fundamento de ser apresentada na aula de 'Desenvolvimento de aplicações rápidas em Python'.", font=('Arial', 12), wraplength=800,justify="center")
        sobre_label.grid(row=0, column=0, padx=10, pady=10)
      
if __name__ == "__main__":
    TelaSobre()
