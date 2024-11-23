from django.urls import path
from .views import LivroList, LivroDetail, AutorDetail, AutorList, CategoriaList, CategoriaDetail, ColecaoListCreateView, ColecaoDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    
    path('livros/', LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),

    
    path('categorias/', CategoriaList.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),

    
    path('autores/', AutorList.as_view(), name='autores-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),

    path('colecoes/', ColecaoListCreateView.as_view(), name='colecao-list-create'),
    path('colecoes/<int:pk>/', ColecaoDetailView.as_view(), name='colecao-detail'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
