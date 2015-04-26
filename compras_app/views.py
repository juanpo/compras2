from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Producto
from django.views import generic

# Create your views here.


class ProductosView(generic.ListView):
    model = Producto
    template_name = 'compras_app/index.html'
    context_object_name = 'productos'
    #queryset = Producto.objects.order_by("descripcion")

class DescripcionAscView(generic.ListView):
	template_name = "compras_app/productos.html"
	context_object_name = "productos"
	queryset = Producto.objects.order_by("descripcion")

class DescripcionDescView(generic.ListView):
	template_name = "compras_app/productos.html"
	context_object_name = "productos"
	queryset = Producto.objects.order_by("-descripcion")

class CodigoDescView(generic.ListView):
	template_name = "compras_app/productos.html"
	context_object_name = "productos"
	queryset = Producto.objects.order_by("-codigo")


def detail(request, codigo):
    descripcion = get_object_or_404(Producto, codigo = codigo)
    return render(request, "compras_app/detail.html", {"codigo": codigo, "descripcion": descripcion})