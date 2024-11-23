from rest_framework import serializers
from .models import Livro, Colecao, Autor, Categoria

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ColecaoSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(many=True)
    colecionador = serializers.StringRelatedField()  
    class Meta:
        model = Colecao
        fields = '__all__'