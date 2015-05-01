from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Producto
from django.views import generic
from django.views.generic.list import MultipleObjectMixin
from braces.views import OrderableListMixin
from compras_app.utils import get_query

# Create your views here.


class ProductosView(OrderableListMixin, generic.ListView):
    model = Producto
    template_name = 'compras_app/productos.html'
    context_object_name = 'productos'
    paginate_by = 100
    orderable_columns = (u"codigo", u"descripcion",)
    orderable_columns_default = u"codigo"
    
def detail(request, codigo):
    descripcion = get_object_or_404(Producto, codigo = codigo)
    return render(request, "compras_app/detail.html", {"codigo": codigo, "descripcion": descripcion})
