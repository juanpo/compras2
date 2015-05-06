from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Producto
from django.views.generic import ListView
from braces.views import OrderableListMixin
from compras_app.utils import get_query
from compras_app.forms import CrearForm

# Create your views here.


class ProductosView(OrderableListMixin, ListView):
    model = Producto
    template_name = 'compras_app/productos.html'
    context_object_name = 'productos'
    paginate_by = 50
    orderable_columns = (u"codigo", u"descripcion",)
    orderable_columns_default = u"descripcion"

class SearchView(ListView):
    model = Producto
    template_name = "compras_app/search_results.html"
    paginate_by = 50
    context_object_name = "found_entries"

    def get_queryset(self):
        found_entries = ""
        query_string = ""
        entry_query = ""
        queryset = super(SearchView, self).get_queryset()

        if ('q' in self.request.GET) and self.request.GET['q'].strip():
        
            query_string = self.request.GET['q']
            entry_query = get_query(query_string, ['descripcion', 'codigo'])
            found_entries = Producto.objects.filter(entry_query).order_by("descripcion")

        if ("ordering" in self.request.GET) and ("order_by" in self.request.GET) and self.request.GET["q"] != "":
            #ya estando los dos, se desarrolla la logica.
            campo = self.request.GET["order_by"]
            sentido = self.request.GET["ordering"]
            #se le asigna el valor a cada una

            if (sentido == "asc"):
                found_entries = Producto.objects.filter(entry_query).order_by(campo)

            else:
                found_entries = Producto.objects.filter(entry_query).order_by("-" + campo)

        queryset = found_entries
        return queryset

def detail(request, codigo):
    descripcion = get_object_or_404(Producto, codigo = codigo)
    return render(request, "compras_app/detail.html", {"codigo": codigo, "descripcion": descripcion})

def crear(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CrearForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            codigo = form.cleaned_data['codigo']
            descripcion = form.cleaned_data["descripcion"]
            producto = Producto.objects.filter(codigo=codigo)

            if producto:
                form.add_error("codigo","Este codigo ya existe")
            else:
                return HttpResponse("no existe")




            # redirect to a new URL:
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CrearForm()

    return render(request, 'compras_app/crear.html', {'form': form})

