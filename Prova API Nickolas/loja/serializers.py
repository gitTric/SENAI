from rest_framework import serializers
from loja.models import Produto, Compra

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
        read_only_fields = ['usuario', 'data_compra']

    def validate(self, data):
        produto = data['produto']
        if produto.quantidade_em_estoque <= 0:
            raise serializers.ValidationError("Não há mais deste produto disponível em nossa loja.")
        return data
    
    def create(self, validated_data):
        produto = validated_data['produto']
        quantidade = validated_data['quantidade']
        produto.quantidade_em_estoque -= quantidade
        produto.save()
        return super().create(validated_data)
    
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

    def validate_quantidade_em_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("A quantidade de produtos não pode ser menor do que 0.")
        return value
