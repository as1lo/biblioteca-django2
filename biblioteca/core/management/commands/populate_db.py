from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro

class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):

        categoria_misterio = Categoria.objects.create(nome="Mistério")
        categoria_ficcao = Categoria.objects.create(nome="Ficção")
      
        autor_agatha = Autor.objects.create(nome="Agatha Christie")
        autor_asimov = Autor.objects.create(nome="Isaac Asimov")
        
        Livro.objects.create(
            titulo="Assassinato no Expresso do Oriente", 
            autor=autor_agatha, 
            categoria=categoria_misterio, 
            publicado_em="1934-01-01"
        )
        Livro.objects.create(
            titulo="Fundação", 
            autor=autor_asimov, 
            categoria=categoria_ficcao, 
            publicado_em="1951-06-01"
        )
