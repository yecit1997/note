from django.shortcuts import render, redirect
from . models import Nota
from .forms import NotaForm
from django.core.paginator import Paginator

def index(request):
    notas = Nota.objects.all()
    paginador = Paginator(notas, 6)
    
    numero_pagina = request.GET.get('page')
    page_obj = paginador.get_page(numero_pagina)

    context = {'page_obj': page_obj}
    return render(request, 'notas/index.html', context)


def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NotaForm()
    context = {'form': form}
    return render(request, 'notas/crear_nota.html', context)


def detalle_nota(request, pk):
    nota = Nota.objects.get(id=pk)
    context = {'nota': nota}
    print(nota.pk)
    return render(request, 'notas/detalle_nota.html', context)
    # return redirect('index')
