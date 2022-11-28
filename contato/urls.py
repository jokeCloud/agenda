from django.urls import path

from .views import index, ver_contato

urlpatterns = [
    path('', index, name='index'),
    path('<int:contato_id>', ver_contato, name='ver_contato'),
]
