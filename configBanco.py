import psycopg2

class BancoDados:
    def __init__(self, banco, usuario, senha):
        self.banco = banco
        self.usuario = usuario
        self.senha = senha
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                dbname=self.banco, user=self.usuario, password=self.senha)
            self.cursor = self.conexao.cursor()
            return True
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False

    def desconectar(self):
        if self.conexao:
            self.cursor.close()
            self.conexao.close()

    def executar_consulta(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conexao.commit()
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Erro ao executar consulta: {e}")
            return None

    def buscar_aluno_por_nome(self, nome_aluno):
        try:
            self.cursor.execute(
                "SELECT id FROM alunos WHERE nome = %s", (nome_aluno,))
            aluno = self.cursor.fetchone()
            if aluno:
                return aluno[0]
            else:
                print(f"Aluno com o nome '{nome_aluno}' não encontrado.")
                return None
        except psycopg2.Error as e:
            print(f"Erro ao buscar aluno: {e}")
            return None

    def buscar_aluno_por_matricula(self, matricula):
        try:
            self.cursor.execute(
                "SELECT id FROM alunos WHERE matricula = %s", (matricula,))
            aluno = self.cursor.fetchone()
            if aluno:
                return aluno[0]
            else:
                print(f"Aluno com a matrícula '{matricula}' não encontrado.")
                return None
        except psycopg2.Error as e:
            print(f"Erro ao buscar aluno por matrícula: {e}")
            return None

    def atualizar_materia(self, aluno_id, sm1, sm2, av, avs, nf, aprovacao):
        try:
            self.cursor.execute("""
                UPDATE materias
                SET sm1 = %s, sm2 = %s, av = %s, avs = %s, nf = %s, aprovacao = %s
                WHERE aluno_id = %s
            """, (sm1, sm2, av, avs, aluno_id, nf, aprovacao))
            self.conexao.commit()
        except psycopg2.Error as e:
            print(f"Erro ao atualizar dados da matéria: {e}")
    
    def deletar_aluno_materia(self, aluno_id):
        try:
            # Deleta as matérias do aluno
            self.cursor.execute("DELETE FROM materias WHERE aluno_id = %s", (aluno_id,))
            # Deleta o aluno
            self.cursor.execute("DELETE FROM alunos WHERE id = %s", (aluno_id,))
            self.conexao.commit()
        except psycopg2.Error as e:
            print(f"Erro ao deletar aluno e suas matérias: {e}")