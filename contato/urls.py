from django.urls import path

from .views import busca, index, ver_contato

urlpatterns = [
    path('', index, name='index'),
    path('busca/', busca, name='busca'),
    path('<int:contato_id>', ver_contato, name='ver_contato'),
]
