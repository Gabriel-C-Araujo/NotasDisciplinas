import tkinter as tk
from tkinter import ttk, messagebox
from configBanco import BancoDados
import filtroDisciplina as FiltraDisciplina
import home as PagHome

class ListaDisciplina:
    def __init__(self,disciplina):
        self.root = tk.Tk()
        self.root.title("Lista de Alunos")
        
        # Define o tamanho da janela
        largura = 800
        altura = 600

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

        # Adiciona a barra de rolagem
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        # Cria a árvore de dados
        self.tree = ttk.Treeview(frame, columns=('Nome', 'Matrícula', 'Matéria', 'Ano', 'Semestre', 'Aprovação', 'SM1', 'SM2', 'AV', 'AVS', 'NF'),
                                  show='headings', yscrollcommand=scrollbar.set)
        
        # Define os cabeçalhos das colunas
        self.tree.heading('Nome', text='Nome', anchor=tk.CENTER)
        self.tree.heading('Matrícula', text='Matrícula', anchor=tk.CENTER)
        self.tree.heading('Matéria', text='Matéria', anchor=tk.CENTER)
        self.tree.heading('Ano', text='Ano', anchor=tk.CENTER)
        self.tree.heading('Semestre', text='Semestre', anchor=tk.CENTER)
        self.tree.heading('Aprovação', text='Aprovação', anchor=tk.CENTER)
        self.tree.heading('SM1', text='SM1', anchor=tk.CENTER)
        self.tree.heading('SM2', text='SM2', anchor=tk.CENTER)
        self.tree.heading('AV', text='AV', anchor=tk.CENTER)
        self.tree.heading('AVS', text='AVS', anchor=tk.CENTER)
        self.tree.heading('NF', text='NF', anchor=tk.CENTER)

        # Define a largura das colunas
        self.tree.column('Nome', width=100)
        self.tree.column('Matrícula', width=100)
        self.tree.column('Matéria', width=100)
        self.tree.column('Ano', width=50)
        self.tree.column('Semestre', width=50)
        self.tree.column('Aprovação', width=50)
        self.tree.column('SM1', width=50)
        self.tree.column('SM2', width=50)
        self.tree.column('AV', width=50)
        self.tree.column('AVS', width=50)
        self.tree.column('NF', width=50)

        # Adiciona a barra de rolagem e a árvore de dados ao frame
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botão de voltar
        homepage_button = ttk.Button(self.root, text="Voltar", command=self.root.destroy , style='Estilo.TButton')
        homepage_button.pack(pady=10)   

        # Preenche a árvore de dados com os alunos e suas matérias
        self.bd = BancoDados()
        self.carregar_alunos_materias(disciplina)
        
        # Centraliza o frame na janela
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        self.root.mainloop()

        checar_home2 = PagHome.TelaHome.__getstate__(self)
        if checar_home2:
            PagHome.TelaHome()        

    def carregar_alunos_materias(self, disciplina):
        if not self.bd.conectar():
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
            return
        try:
            print(disciplina)
            # Consulta para obter os alunos e suas matérias
            self.bd.cursor.execute("""
            SELECT alunos.nome, alunos.matricula, materias.nome_da_materia, materias.ano, materias.semestre, materias.aprovacao,
            materias.sm1, materias.sm2, materias.av, materias.avs, materias.nf
            FROM alunos
            JOIN materias ON alunos.id = materias.aluno_id
            WHERE materias.nome_da_materia = %s
            """,(disciplina,))
            alunos_disciplina = self.bd.cursor.fetchall()
            # Preenche a árvore de dados com os alunos e suas matérias
            # não ta funcionando
            for aluno_materia in alunos_disciplina:
                self.tree.insert('', tk.END, values=aluno_materia)
        finally:
            self.bd.desconectar()

if __name__ == "__main__":
    ListaDisciplina()
