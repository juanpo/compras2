from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from models import Producto
from django.views.generic import ListView, DetailView
from braces.views import OrderableListMixin
from compras_app.utils import get_query
from compras_app.forms import CrearForm
from django.views.generic.edit import DeleteView, UpdateView, CreateView
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

class ProductosSearchView(ListView):
    model = Producto
    template_name = "compras_app/search_results.html"
    paginate_by = 50
    context_object_name = "found_entries"

    def get_queryset(self):
        found_entries = ""
        query_string = ""
        entry_query = ""
        queryset = super(ProductosSearchView, self).get_queryset()

        if ('q' in self.request.GET) and self.request.GET['q'].strip():
        
            query_string = self.request.GET['q']
            entry_query = get_query(query_string, ['descripcion', 'codigo'])
            found_entries = Producto.objects.filter(entry_query).order_by("descripcion")

        if ("ordering" in self.request.GET) and ("order_by" in self.request.GET) and (self.request.GET["q"] != ""):
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

class ProductosBorrarView(DeleteView):
    model = Producto
    success_url = "/productos/"
    success_message = "El producto fue borrado satisfactoriamente."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductosBorrarView, self).delete(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Producto, pk=Producto.objects.filter(codigo=self.kwargs["codigo"]))

class ProductosDetalleView(DetailView):
    model = Producto
    template_name = "compras_app/detail.html"

    def get_object(self):
        return get_object_or_404(Producto, pk=Producto.objects.filter(codigo=self.kwargs["codigo"]))

class ProductosEditarView(SuccessMessageMixin, UpdateView):
    model = Producto
    fields = ['descripcion']
    template_name = "compras_app/producto_update_form.html"
    success_url = "/productos/"
    success_message = "El producto fue editado satisfactoriamente."   

    def get_object(self):
        return get_object_or_404(Producto, pk=Producto.objects.filter(codigo=self.kwargs["codigo"]))

class ProductosCrearView(SuccessMessageMixin, CreateView):
    model = Producto
    template_name = "compras_app/crear.html"
    fields = ["codigo", "descripcion"]
    success_url = "/productos/"
    success_message = "El producto fue creado con exito."

def handle(request, codigo):
    if request.method == "POST":

        if "borrar" in request.POST:
            return HttpResponseRedirect("/productos/"+codigo+"/borrar")

        if "editar" in request.POST:
            return HttpResponseRedirect("/productos/"+codigo+"/editar")

    else:
        raise Http404("Esta pagina no existe.")        

