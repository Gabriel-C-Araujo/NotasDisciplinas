import tkinter as tk
from tkinter import ttk, messagebox
from configBanco import BancoDados
from PIL import Image, ImageTk
from home import TelaHome

class TelaLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tela de Login")
        
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
        estilo.configure('Estilo.TButton', foreground="black", font=('Arial', 10), background='#0074D9')  # Azul

        # Carrega a imagem e a exibe centralizada
        imagem = self.carregar_imagem("imagens/logo.png", 200, 200)
        imagem_label = tk.Label(self.root, image=imagem)
        imagem_label.image = imagem
        imagem_label.pack(pady=10)

        # Labels e Entry para username e password
        tk.Label(self.root, text="Username:", font=('Arial', 12)).pack()
        self.username_entry = ttk.Entry(self.root, style='Estilo.TEntry')
        self.username_entry.pack()

        tk.Label(self.root, text="Password:", font=('Arial', 12)).pack()
        self.password_entry = ttk.Entry(self.root, show="*", style='Estilo.TEntry')
        self.password_entry.pack()

        # Botão de login
        login_button = ttk.Button(self.root, text="Login", command=self.fazer_login, style='Estilo.TButton')
        login_button.pack(pady=10)

        # Botão de fechar
        close_button = ttk.Button(self.root, text="Fechar", command=self.fechar_janela, style='Estilo.TButton')
        close_button.pack(pady=5)

        self.bd = BancoDados("SistemaNotas", "postgres", "123456")
        self.root.mainloop()

    def carregar_imagem(self, caminho, largura, altura):
        imagem = Image.open(caminho)
        imagem = imagem.resize((largura, altura), Image.ANTIALIAS)
        return ImageTk.PhotoImage(imagem)

    def fazer_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        autenticar_usuario(username, password)

    def fechar_janela(self):
        self.root.destroy()

def autenticar_usuario(username, password):
    bd = BancoDados("SistemaNotas", "postgres", "123456")
    if not bd.conectar():
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
        return

    try:
        # Consulta SQL para verificar se o usuário e senha estão corretos
        result = bd.executar_consulta("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
        if result:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            # Chama a tela home
            TelaHome()
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos!")
    finally:
        bd.desconectar()

if __name__ == "__main__":
    TelaLogin()
