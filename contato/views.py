from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Contato


# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contato/index.html', context={
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contato/ver_contato.html', context={
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')

    contatos = Contato.objects.order_by('-id').filter(
        nome__icontains=termo,
        mostrar=True
    )
    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contato/busca.html', context={
        'contatos': contatos
    })
