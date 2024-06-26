import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from configBanco import BancoDados 

class AtualizaAluno:
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

        # Labels e Entry para nome do aluno
        nome_label = ttk.Label(frame, text="Nome do Aluno:", font=('Arial', 12))
        nome_label.grid(row=0, column=0, padx=10, pady=10)

        self.nome_entry = ttk.Entry(frame, font=('Arial', 12))
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        # Labels e Entry para SM1
        sm1_label = ttk.Label(frame, text="SM1:", font=('Arial', 12))
        sm1_label.grid(row=1, column=0, padx=10, pady=10)

        self.sm1_entry = ttk.Entry(frame, font=('Arial', 12))
        self.sm1_entry.grid(row=1, column=1, padx=10, pady=10)

        # Labels e Entry para SM2
        sm2_label = ttk.Label(frame, text="SM2:", font=('Arial', 12))
        sm2_label.grid(row=2, column=0, padx=10, pady=10)

        self.sm2_entry = ttk.Entry(frame, font=('Arial', 12))
        self.sm2_entry.grid(row=2, column=1, padx=10, pady=10)

        # Labels e Entry para AV
        av_label = ttk.Label(frame, text="AV:", font=('Arial', 12))
        av_label.grid(row=3, column=0, padx=10, pady=10)

        self.av_entry = ttk.Entry(frame, font=('Arial', 12))
        self.av_entry.grid(row=3, column=1, padx=10, pady=10)

        # Labels e Entry para AVS
        avs_label = ttk.Label(frame, text="AVS:", font=('Arial', 12))
        avs_label.grid(row=4, column=0, padx=10, pady=10)

        self.avs_entry = ttk.Entry(frame, font=('Arial', 12))
        self.avs_entry.grid(row=4, column=1, padx=10, pady=10)

        # Botão de atualizar
        atualizar_button = ttk.Button(frame, text="Atualizar", command=self.atualizar_aluno, style='Estilo.TButton')
        atualizar_button.grid(row=5, column=0, padx=10, pady=10)

        # Botão de deletar
        deletar_button = ttk.Button(frame, text="Deletar", command=self.deletar_aluno, style='Estilo.TButton')
        deletar_button.grid(row=5, column=1, padx=10, pady=10)

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

    def atualizar_aluno(self):
        # Função para atualizar as informações do aluno
        nome_aluno = self.nome_entry.get()
        sm1 = self.sm1_entry.get()
        sm2 = self.sm2_entry.get()
        av = self.av_entry.get()
        avs = self.avs_entry.get()
        aprovacao = False
        nf = '0'

        if av > avs:
            if av == '10':
                nf = av
                aprovacao = True
                self.popup_aprovado()
            if float(av) > 6: 
               nf = (av + sm1 + sm2)
               if nf > '10':
                   nf = '10'
                   self.popup_aprovado()
               aprovacao = True
               self.popup_aprovado()
            else:
                self.popup_reprovado()
        else :
            if avs == '10':
                nf = avs
                aprovacao = True
                self.popup_aprovado()
            if float(av) > 6:
               nf = (avs + sm1 + sm2)
               aprovacao = True
               self.popup_aprovado()
               if nf > '10':
                   nf = '10'
                   self.popup_aprovado()
               aprovacao = True
            else:
                self.popup_reprovado()

        if self.bd.conectar():
            aluno_id = self.bd.buscar_aluno_por_nome(nome_aluno)
            if aluno_id:
                self.bd.atualizar_materia(aluno_id, sm1, sm2, av, avs, nf , aprovacao)
                messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso.")
                self.root.destroy()
            else:
                messagebox.showerror("Erro", "Aluno não encontrado.")
                self.root.focus_force()
            self.bd.desconectar()

    def deletar_aluno(self):
        # Função para deletar as informações do aluno
        nome_aluno = self.nome_entry.get()

        if self.bd.conectar():
            aluno_id = self.bd.buscar_aluno_por_nome(nome_aluno)
            if aluno_id:
                self.bd.deletar_aluno_materia(aluno_id)
                messagebox.showinfo("Sucesso", "Aluno deletado com sucesso.")
                self.root.destroy()
            else:
                messagebox.showerror("Erro", "Aluno não encontrado.")
                self.root.focus_force()
            self.bd.desconectar()
    
    @staticmethod
    def popup_aprovado():
        showinfo("Window", "Aprovado!")

    @staticmethod
    def popup_reprovado():
        showinfo("Window", "Reprovado!")

if __name__ == "__main__":
    AtualizaAluno()
