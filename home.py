import tkinter as tk
from tkinter import ttk
from cadastroAluno import TelaCadastroAluno
from cadastroUsuario import TelaCadastroUsuario
import listaAlunos as ListaAluno
from sobre import TelaSobre

class TelaHome:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tela Home")
        
        # Define o tamanho da janela e a centraliza na tela
        largura = 500
        altura = 450
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

        # Estilo para os campos de entrada e botão
        estilo = ttk.Style()
        estilo.configure('Estilo.TEntry', foreground="black", font=('Arial', 10))
        estilo.configure('Estilo.TButton', foreground="black", font=('Arial', 10), background='#0074D9')

        # Botões "Cadastrar Aluno", "Listar Alunos", "Cadastrar Usuário" e "Fazer Logout"
        cadastrar_aluno_button = ttk.Button(self.root, text="Cadastrar Aluno", command=self.abrir_tela_cadastro_aluno, style='Estilo.TButton')
        cadastrar_aluno_button.pack(pady=10)

        listar_alunos_button = ttk.Button(self.root, text="Listar Alunos", command=self.abrir_tela_lista_alunos, style='Estilo.TButton')
        listar_alunos_button.pack(pady=10)

        cadastrar_usuario_button = ttk.Button(self.root, text="Cadastrar Usuário", command=self.abrir_tela_cadastro_usuario, style='Estilo.TButton')
        cadastrar_usuario_button.pack(pady=10)

        sobre_button = ttk.Button(self.root, text="Sobre", command=self.abrir_tela_sobre, style='Estilo.TButton')
        sobre_button.pack(pady=10)

        logout_button = ttk.Button(self.root, text="Fazer Logout", command=self.fazer_logout, style='Estilo.TButton')
        logout_button.pack(pady=10)

        self.root.mainloop()

    def abrir_tela_cadastro_aluno(self):
        TelaCadastroAluno()    

    def abrir_tela_lista_alunos(self):
        self.root.destroy()
        ListaAluno.ListaDeAlunos()

    def abrir_tela_cadastro_usuario(self):
        TelaCadastroUsuario()

    def abrir_tela_sobre(self):
        TelaSobre()

    def fazer_logout(self):
        self.root.destroy()    

if __name__ == "__main__":
    TelaHome()
