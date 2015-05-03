from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Producto
from django.views import generic
from braces.views import OrderableListMixin
from compras_app.utils import get_query

# Create your views here.


class ProductosView(OrderableListMixin, generic.ListView):
    model = Producto
    template_name = 'compras_app/productos.html'
    context_object_name = 'productos'
    paginate_by = 100
    orderable_columns = (u"codigo", u"descripcion",)
    orderable_columns_default = u"descripcion"
    
def detail(request, codigo):
    descripcion = get_object_or_404(Producto, codigo = codigo)
    return render(request, "compras_app/detail.html", {"codigo": codigo, "descripcion": descripcion})

def search(request):
    query_string = ''
    found_entries = None
    
    if ('q' in request.GET) and request.GET['q'].strip():
        
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['descripcion', 'codigo'])
        found_entries = Producto.objects.filter(entry_query).order_by('descripcion')

    if ("ordering" in request.GET) and ("order_by" in request.GET):
        #ya estando los dos, se desarrolla la logica.
        campo = request.GET["order_by"]
        sentido = request.GET["ordering"]
        #se le asigna el valor a cada una

        if (sentido == "asc"):
            found_entries = Producto.objects.filter(entry_query).order_by(campo)

        else:
            found_entries = Producto.objects.filter(entry_query).order_by("-" + campo)

    return render(request, 'compras_app/search_results.html', {
		'query_string': query_string,
		'found_entries': found_entries,
		})
