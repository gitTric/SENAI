from django.shortcuts import render

from rest_framework import generics
from loja.models import Compra
from loja.serializers import CompraSerializer
from loja.models import Produto
from loja.serializers import ProdutoSerializer
from rest_framework.permissions import IsAuthenticated

class CompraAPIView(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ProdutoAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]
