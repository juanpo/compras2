from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import Producto


def index(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'compras_app/index.html', context)

def detail(request, codigo):
    return HttpResponse("Estas viendo el producto del codigo %s." % codigo)