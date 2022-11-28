from django.shortcuts import render

from .models import Contato


# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contato/index.html', context={
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render(request, 'contato/ver_contato.html', context={
        'contato': contato
    })
