from django.contrib import admin

from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email',
                    'telefone', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('nome', 'sobrenome')
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'email', 'telefone')
    list_editable = ('telefone', 'mostrar')


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
