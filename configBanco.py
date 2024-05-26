import psycopg2

class BancoDados:
    def __init__(self):#, banco, usuario, senha):
        self.conexao = psycopg2.connect(database="SistemaNotas", user="postgres", password="123456", host="localhost", port=5432)
        self.cursor = None

    def conectar(self):
        try:
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

    # Não sei se ta funcionando 100%, n quer buscar por nada    
    def buscar_aluno_por_disciplina(self, nome_disciplina):
        try:
            self.cursor.execute(
                "SELECT id FROM materias WHERE nome_da_materia = %s", (nome_disciplina,))
            disciplina = self.cursor.fetchone()
            if disciplina:
                return disciplina[0]
            else:
                print(f"Disciplina '{nome_disciplina}' não encontrada.")
                return None
        except psycopg2.Error as e:
            print(f"Erro ao buscar disciplina: {e}")
            return None
    
    def atualizar_materia(self, aluno_id, sm1, sm2, av, avs, nf, aprovacao):
        try:
            self.cursor.execute("""
                UPDATE materias
                SET sm1 = %s, sm2 = %s, av = %s, avs = %s, nf = %s, aprovacao = %s
                WHERE aluno_id = %s
            """, (sm1, sm2, av, avs, nf, aprovacao, aluno_id))
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

    def criar_banco_dados(self):
        try:
            self.cursor.execute('''
            CREATE DATABASE IF NOT EXISTS SistemaNotas;

            --CREATE SCHEMA IF NOT EXISTS SistemaNotas;
                                                    
            CREATE TABLE IF NOT EXISTS login (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(100) NOT null);

            -- Criação da tabela alunos
            CREATE TABLE IF NOT EXISTS alunos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            matricula VARCHAR(20) UNIQUE NOT NULL
            );

            -- Criação da tabela materias
            CREATE TABLE IF NOT EXISTS materias (
            id SERIAL PRIMARY KEY,
            aluno_id INTEGER REFERENCES alunos(id),
            nome_da_materia VARCHAR(100) NOT NULL,
            ano INTEGER NOT NULL,
            semestre INTEGER NOT NULL,
            aprovacao BOOLEAN NOT NULL DEFAULT FALSE,
            sm1 FLOAT,
            sm2 FLOAT,
            av FLOAT,
            avs FLOAT,
            nf FLOAT,
            CONSTRAINT fk_aluno FOREIGN KEY (aluno_id) REFERENCES alunos(id) ON DELETE CASCADE
            );

            INSERT INTO public.login
            (id, username, "password")
            VALUES(nextval('login_id_seq'::regclass), 'admin', '123456') ON CONFLICT DO NOTHING;''')
            self.conexao.commit()
        except psycopg2.Error as e:
            print(f"Erro ao criar as tabelas e inserir os dados do usuário inicial: {e}")