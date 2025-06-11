import sqlite3

class ProdutoDAO:
    def __init__(self):
        self.conn = sqlite3.connect("database/estoque.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
        )
        """)

    def cadastrar_prod(self, produto):
        self.cursor.execute("""
        INSERT INTO produtos(nome, quantidade, preco)
        VALUES(?,?,?)
        """, (produto.nome, produto.quantidade, produto.preco))

        self.conn.commit()

    def listar_prod(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()
    
    def atualizar_prod(self, nome, novaQuantidade, novoPreco):
        self.cursor.execute("""
        UPDATE
            produtos
        SET
            quantidade = (?), preco = (?)
        WHERE
            nome = (?)
        """, (novaQuantidade, novoPreco, nome))
        self.conn.commit()

    def deletar_prod(self, nome):
        self.cursor.execute("""
        DELETE FROM
            produtos
        WHERE
            nome = (?)
        """, (nome,))
        
        self.conn.commit()

    def cosultar_nome(self, nome):
        self.cursor.execute("SELECT * FROM produtos WHERE nome = (?)", (nome,))
        return self.cursor.fetchall()
    
    def consultar_id(self, id):
        self.cursor.execute("SELECT * FROM produtos WHERE id = (?)", (id,))
        return self.cursor.fetchall()
    
    def valor_total(self):
        self.cursor.execute("""
        SELECT
            SUM(quantidade * preco) AS total_estoque
        FROM
            produtos
        """)
        return self.cursor.fetchall()
