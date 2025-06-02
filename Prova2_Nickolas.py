#CONECTANDO O SQLITE3
import sqlite3

conect = sqlite3.connect("loja.db")
cursor = conect.cursor()

#CRIANDO A TABELA
cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL         
);
""")

#FUNÇÃO PARA ADICIONAR PRODUTOS
def adicionarProduto():
    print("----------------------------------------------")
    nome = input("Informe o nome do produto a ser adicionado: ")
    preco = float(input("Informe o preço do produto a ser adicionado: "))
    quantidade = int(input("Informe a quantidade presente no seu estoque deste produto: "))

    if preco < 0:
        print("O preço informado é inválido! Esse produto não será salvo!!")
        menu()
    if quantidade < 0:
        print("O estoque informado é inválido! Esse produto não será salvo!!")
        menu()

    cursor.execute("""
    INSERT INTO Produtos(nome, preco, quantidade)
    VALUES(?,?,?);
    """, (nome, preco, quantidade))

    conect.commit()
    print("Produto salvo com sucesso no banco de dados!")

#FUNÇÃO PARA LISTAR TODOS OS PRODUTOS NO BANCO DE DADOS
def listarProduto():
    print("----------------------------------------------")
    cursor.execute("SELECT * FROM Produtos;")
    dados = cursor.fetchall()

    print("LISTA DE PRODUTOS:")
    print("")
    for produtos in dados:
        print(produtos)

#FUNÇÃO PARA ATUALIZAR UM PRODUTO DENTRO DA TABELA
def atualizarProduto():
    print("----------------------------------------------")
    nome = input("Informe o nome do produto a ser alterado: ")
    preco = float(input("Informe o novo preço do produto: "))
    quantidade = int(input("Informe a nova quantidade do produto presente no estoque: "))

    cursor.execute("""
    UPDATE
        Produtos
    SET
        preco = (?), quantidade = (?)
    WHERE
        nome = (?);
    """, (preco, quantidade, nome))

    conect.commit()
    print("Produto atualizado!")

#FUNÇÃO PARA DELETAR UM PRODUTO
def removerProduto():
    print("----------------------------------------------")
    nome = input("Informe o nome do produto a ser deletado: ")

    cursor.execute("""
    DELETE FROM
        Produtos
    WHERE
        nome = (?);  
    """, (nome,))

    conect.commit()
    print("Produto removido!")

#FUNÇÃO PARA NUSCAR UM PRODUTO ESPECÍFICO
def buscarProduto():
    print("----------------------------------------------")
    nome = input("Informe o nome do produto a ser procurado: ")

    cursor.execute("""
    SELECT * FROM Produtos WHERE nome = (?)
    """, (nome,))
    dados = cursor.fetchall()
    for produto in dados:
        print(produto)

def menu():
    while True:
        print("----------------------------------------------")
        print("MENU ESTOQUE")
        print("----------------------------------------------")
        print("")

        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        print("")
        escolha = int(input("Escolha uma das opções acima (1, 2, 3, 4, 5 ou 6): "))

        if escolha == 1:
            adicionarProduto()
        if escolha == 2:
            listarProduto()
        if escolha == 3:
            atualizarProduto()
        if escolha == 4:
            removerProduto()
        if escolha == 5:
            buscarProduto()
        if escolha == 6:
            print("Saindo...")
            conect.close()
            break

#CHAMANDO FUNÇÃO PRINCIPAL
menu()