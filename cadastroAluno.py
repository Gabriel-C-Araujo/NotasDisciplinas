import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from configBanco import BancoDados

class TelaCadastroAluno:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Aluno")
        
        # Define o tamanho da janela
        largura = 500
        altura = 300

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

        # Estilo para os campos de entrada e botão
        estilo = ttk.Style()
        estilo.configure('Estilo.TEntry', foreground="black", font=('Arial', 10))
        estilo.configure('Estilo.TButton', foreground="white", font=('Arial', 10), background='#4CAF50')

        # Labels e Entry para nome e matrícula do aluno
        nome_label = ttk.Label(frame, text="Nome:", font=('Arial', 12))
        nome_label.grid(row=0, column=0, padx=10, pady=10)

        self.nome_entry = ttk.Entry(frame, style='Estilo.TEntry')
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        matricula_label = ttk.Label(frame, text="Matrícula:", font=('Arial', 12))
        matricula_label.grid(row=1, column=0, padx=10, pady=10)

        self.matricula_entry = ttk.Entry(frame, style='Estilo.TEntry')
        self.matricula_entry.grid(row=1, column=1, padx=10, pady=10)

        # Labels e Entry para nome da matéria, ano e semestre
        materia_label = ttk.Label(frame, text="Nome da Matéria:", font=('Arial', 12))
        materia_label.grid(row=2, column=0, padx=10, pady=10)

        self.materia_entry = ttk.Entry(frame, style='Estilo.TEntry')
        self.materia_entry.grid(row=2, column=1, padx=10, pady=10)

        ano_label = ttk.Label(frame, text="Ano:", font=('Arial', 12))
        ano_label.grid(row=3, column=0, padx=10, pady=10)

        self.ano_entry = ttk.Entry(frame, style='Estilo.TEntry')
        self.ano_entry.grid(row=3, column=1, padx=10, pady=10)

        semestre_label = ttk.Label(frame, text="Semestre:", font=('Arial', 12))
        semestre_label.grid(row=4, column=0, padx=10, pady=10)

        self.semestre_entry = ttk.Entry(frame, style='Estilo.TEntry')
        self.semestre_entry.grid(row=4, column=1, padx=10, pady=10)

        # Botão de cadastrar
        cadastrar_button = ttk.Button(frame, text="Cadastrar", command=self.cadastrar_aluno, style='Estilo.TButton')
        cadastrar_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

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

    def cadastrar_aluno(self):
        nome = self.nome_entry.get()
        matricula = self.matricula_entry.get()
        materia = self.materia_entry.get()
        ano = self.ano_entry.get()
        semestre = self.semestre_entry.get()

        if not self.bd.conectar():
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
            return

        try:
            # Verifica se a matrícula já existe na tabela de alunos
            result = self.bd.executar_consulta("SELECT * FROM alunos WHERE matricula = %s", (matricula,))
            if result:
                messagebox.showerror("Erro", "Esta matrícula já está em uso!")
            else:
                # Insere o novo aluno na tabela
                self.bd.executar_consulta("INSERT INTO alunos (nome, matricula) VALUES (%s, %s)", (nome, matricula))
                
                # Obtém o ID do aluno recém-inserido
                aluno_id = self.bd.buscar_aluno_por_matricula(matricula)
                
                if aluno_id:
                    # Insere a nova matéria para o aluno na tabela de matérias
                    self.bd.executar_consulta("INSERT INTO materias (aluno_id, nome_da_materia, ano, semestre) VALUES (%s, %s, %s, %s)",
                                                (aluno_id, materia, ano, semestre))
                    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
                else:
                    messagebox.showerror("Erro", "Não foi possível obter o ID do aluno.")
        finally:
            self.bd.desconectar()

if __name__ == "__main__":
    TelaCadastroAluno()
