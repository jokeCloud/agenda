from django.urls import path

from .views import cadastro, dashboard, login, logout

urlpatterns = [
    path('', login, name='index_login'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
    path('dashboard/', dashboard, name='dashboard'),
]
