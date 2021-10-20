from django.shortcuts import render, redirect
from app.form import CarroForm
from app.models import Carro
from django.core.paginator import Paginator
# Create your views here.

"""
#esta função faz busca por pagina
def page(request):
    data = {}
    all = Carro.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)
"""

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carro.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carro.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = CarroForm
    return render(request, 'form.html', data)


def create(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carro.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Carro.objects.get(pk=pk)
    data['form'] = CarroForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Carro.objects.get(pk=pk)
    form = CarroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    data = {}
    data['db'] = Carro.objects.get(pk=pk).delete()
    return redirect('home')
