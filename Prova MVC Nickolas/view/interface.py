from controller.controle_estoque import ControleEstoque

class Interface:
    def __init__(self):
        self.controle = ControleEstoque()

    def menu(self):
        while True:
            print("\n---MENU---")
            print("1. Cadastrar produto")
            print("2. Listar produtos")
            print("3. Atualizar produto")
            print("4. Deletar produto")
            print("5. Consultar por nome")
            print("6. Consultar por id")
            print("7. Valor total no estoque")
            print("8. Sair")

            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                self.cadastrar_prod()
            elif escolha == 2:
                self.listar_prod()
            elif escolha == 3:
                self.atualizar_prod()
            elif escolha == 4:
                self.deletar_prod()
            elif escolha == 5:
                self.consultar_nome()
            elif escolha == 6:
                self.consultar_id()
            elif escolha == 7:
                self.valor_total()
            elif escolha == 8:
                print("Saindo...")
                break
            else:
                print("Opção escolhida é inválida!")

    def cadastrar_prod(self):
        nome = input("Informe o nome do produto: ")
        quantidade = int(input("Informe a quantidade do produto: "))
        preco = float(input("Informe o preço do produto: "))
        mensagem = self.controle.cadastrar_prod(nome, quantidade, preco)
        print(mensagem)

    def listar_prod(self):
        produtos = self.controle.listar_prod()
        print("\n---Produtos Cadastrados---")
        for p in produtos:
            print(f"ID:{p[0]} | Nome: {p[1]} | Quantidade: {p[2]} | Preço: R${p[3]:.2f}")

    def atualizar_prod(self):
        novaQuantidade = int(input("Informe a nova quantidade do produto em estoque: "))
        novoPreco = float(input("Informe o novo preço do produto: "))
        nome = input("Informe o noe do produto a ser alterado: ")
        mensagem = self.controle.atualizar_prod(nome, novaQuantidade, novoPreco)
        print(mensagem)

    def deletar_prod(self):
        nome = input("Informe o nome do produto a ser deletado: ")
        mensagem = self.controle.deletar_prod(nome)
        print(mensagem)

    def consultar_nome(self):
        nome = input("Informe o nome do produto a ser buscado: ")
        mensagem = self.controle.consultar_nome(nome)
        print(mensagem)

    def consultar_id(self):
        id = int(input("Informe o id do produto a ser buscado: "))
        mensagem = self.controle.consultar_id(id)
        print(mensagem)

    def valor_total(self):
        mensagem = self.controle.valor_total()
        print(mensagem)