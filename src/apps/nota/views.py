from django.shortcuts import render, redirect
from .models import Nota
from .forms import NotaForm
from django.core.paginator import Paginator
from django.contrib import messages

# Create function to show all notes
def index(request):
    notas = Nota.objects.all()
    paginador = Paginator(notas, 6)

    numero_pagina = request.GET.get("page")
    page_obj = paginador.get_page(numero_pagina)

    context = {"page_obj": page_obj}
    return render(request, "notas/index.html", context)

# Create function to create notes
def crear_nota(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nota creada con éxito.")
            return redirect("index")
    else:
        form = NotaForm()
    context = {"form": form}
    return render(request, "notas/crear_nota.html", context)

# Create function to see note details
def detalle_nota(request, pk):
    nota = Nota.objects.get(id=pk)
    context = {"nota": nota}
    print(nota.pk)
    return render(request, "notas/detalle_nota.html", context)
    # return redirect('index')

# Create funtion to edit notes
def editar_nota(request, pk):
    nota = Nota.objects.get(id=pk)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            messages.success(request, "Nota editada con éxito.")
            return redirect("index")
    else:
        form = NotaForm(instance=nota)
    context = {"form": form}
    return render(request, "notas/crear_nota.html", context)

# Create function to delete notes
def eliminar_nota(request, pk):
    nota = Nota.objects.get(id=pk)
    if request.method == "POST":
        nota.delete()
        messages.success(request, "Nota eliminada con éxito.")
        return redirect("index")
    context = {"nota": nota}
    return render(request, "notas/eliminar_nota.html", context)