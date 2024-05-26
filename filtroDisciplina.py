import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from configBanco import BancoDados 
import listaDisciplina as ListaDisciplina
import home as PagHome

class FiltraDisciplina:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Atualizar Aluno")
        
        # Define o tamanho da janela
        largura = 500
        altura = 450

        # Estilo para os campos de entrada e botão
        estilo = ttk.Style()
        estilo.configure('Estilo.TEntry', foreground="black", font=('Arial', 10))
        estilo.configure('Estilo.TButton', foreground="black", font=('Arial', 10), background='#0074D9')

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

        # Labels e Entry para nome da disciplina
        disciplina_label = ttk.Label(frame, text="Nome da Disciplina:", font=('Arial', 12))
        disciplina_label.grid(row=0, column=0, padx=10, pady=10)

        self.disciplina_entry = ttk.Entry(frame, font=('Arial', 12))
        self.disciplina_entry.grid(row=0, column=1, padx=10, pady=10)        

        # Botão de filtrar
        filtrar_button = ttk.Button(frame, text="Filtrar", command=self.filtrar_disciplina, style='Estilo.TButton')
        filtrar_button.grid(row=5, column=0, padx=10, pady=10)

        # Centraliza o frame na janela
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_rowconfigure(4, weight=1)
        frame.grid_rowconfigure(5, weight=1)

        self.bd = BancoDados() 
        self.root.mainloop()

    def filtrar_disciplina(self):
        # Função para filtrar por matéria (abre a tela mas tem q terminar, fritei aqui)
        disciplina = self.disciplina_entry.get()        

        if self.bd.conectar():
            disciplina_id = self.bd.buscar_aluno_por_disciplina(disciplina)
            if disciplina_id:
                listaDisciplina = ListaDisciplina.ListaDisciplina()
                self.root.destroy()
            else:
                messagebox.showerror("Erro", "Disciplina não encontrado.")
                self.root.focus_force()

if __name__ == "__main__":
    FiltraDisciplina()
