from model.produto import Produto
from model.produto_dao import ProdutoDAO

class ControleEstoque:
    def __init__(self):
        self.dao = ProdutoDAO()

    def cadastrar_prod(self, nome, quantidade, preco):
        produto = Produto(nome, quantidade, preco)
        if quantidade < 0 or preco < 0:
            return "Os valores informados são inválidos!"
        else:
            self.dao.cadastrar_prod(produto)
            return "Produto cadastrado com sucesso!"
    
    def listar_prod(self):
        return self.dao.listar_prod()
    
    def atualizar_prod(self, nome, novaQuantidade, novoPreco):
        if novaQuantidade < 0 or novoPreco < 0:
            return "Os valores informados são inválidos!"
        else:
            self.dao.atualizar_prod(nome, novaQuantidade, novoPreco)
            return "Produto atualizado com sucesso!"
    
    def deletar_prod(self, nome):
        self.dao.deletar_prod(nome)
        return "Produto deletado com sucesso!"
    
    def consultar_nome(self, nome):
       return self.dao.cosultar_nome(nome)
    
    def consultar_id(self, id):
        return self.dao.consultar_id(id)

    def valor_total(self):
        return self.dao.valor_total()