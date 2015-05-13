from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from models import Producto
from django.views.generic import ListView, DetailView
from braces.views import OrderableListMixin
from compras_app.utils import get_query
from compras_app.forms import CrearForm
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

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

class BorrarProducto(DeleteView):
    model = Producto
    success_url = "/productos/"
    success_message = "El producto fue borrado satisfactoriamente."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BorrarProducto, self).delete(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Producto, pk=Producto.objects.filter(codigo=self.kwargs["codigo"]))

class DetalleProducto(DetailView):
    model = Producto
    template_name = "compras_app/detail.html"

    def get_object(self):
        return get_object_or_404(Producto, pk=Producto.objects.filter(codigo=self.kwargs["codigo"]))

class EditarProducto(SuccessMessageMixin, UpdateView):
    model = Producto
    fields = ['descripcion']
    template_name = "compras_app/producto_update_form.html"
    success_url = "/productos/"
    success_message = "El producto fue editado satisfactoriamente."   

    def get_object(self):
        return get_object_or_404(Producto, pk=Producto.objects.filter(codigo=self.kwargs["codigo"]))
        
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
                objeto = Producto(codigo=codigo, descripcion=descripcion)
                objeto.save()
                return render(request, "compras_app/success.html", {"objeto": objeto})




            # redirect to a new URL:
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CrearForm()

    return render(request, 'compras_app/crear.html', {'form': form})

def handle(request, codigo):
    if request.method == "POST":

        if "borrar" in request.POST:
            return HttpResponseRedirect("/productos/"+codigo+"/borrar")

        if "editar" in request.POST:
            return HttpResponseRedirect("/productos/"+codigo+"/editar")

    else:
        raise Http404("Esta pagina no existe.")        

