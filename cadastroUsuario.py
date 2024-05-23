# cadastroUsuario.py

import tkinter as tk
from tkinter import ttk, messagebox
from configBanco import BancoDados

class TelaCadastroUsuario:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Usuário")
        
        # Define o tamanho da janela
        largura = 500
        altura = 350

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

        # Labels e Entry para nome de usuário, senha e confirmação de senha
        username_label = ttk.Label(frame, text="Nome de Usuário:", font=('Arial', 12))
        username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_entry = ttk.Entry(frame, style='Estilo.TEntry')
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = ttk.Label(frame, text="Senha:", font=('Arial', 12))
        password_label.grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = ttk.Entry(frame, style='Estilo.TEntry', show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        confirm_password_label = ttk.Label(frame, text="Confirme a Senha:", font=('Arial', 12))
        confirm_password_label.grid(row=2, column=0, padx=10, pady=10)

        self.confirm_password_entry = ttk.Entry(frame, style='Estilo.TEntry', show="*")
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Botão de cadastrar
        cadastrar_button = ttk.Button(frame, text="Cadastrar", command=self.cadastrar_usuario, style='Estilo.TButton')
        cadastrar_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


        # Centraliza o frame na janela
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_rowconfigure(4, weight=1)

        self.bd = BancoDados("SistemaNotas", "postgres", "123456")
        self.root.mainloop()

    def cadastrar_usuario(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Erro", "As senhas não correspondem.")
            return

        if not self.bd.conectar():
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
            return

        try:
            # Verifica se o nome de usuário já existe na tabela de login
            result = self.bd.executar_consulta("SELECT * FROM login WHERE username = %s", (username,))
            if result:
                messagebox.showerror("Erro", "Este nome de usuário já está em uso!")
            else:
                # Insere o novo usuário na tabela
                self.bd.executar_consulta("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        finally:
            self.bd.desconectar()

    def voltar(self):
        self.root.destroy()

if __name__ == "__main__":
    TelaCadastroUsuario()
