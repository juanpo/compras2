from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from proveedores_app.models import Proveedor
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from compras_app.utils import get_query
from braces.views import OrderableListMixin


# Create your views here.


class ProveedoresView(OrderableListMixin, ListView):
    model = Proveedor
    template_name = "proveedores_app/proveedores.html"
    context_object_name = 'proveedores'
    orderable_columns = (u"codigo", u"descripcion",)
    orderable_columns_default = u"descripcion"    


class ProveedoresCrearView(SuccessMessageMixin, CreateView):
	model = Proveedor
	template_name = "proveedores_app/proveedores_create_form.html"
	fields = ["codigo", "descripcion"]
	success_url = "/proveedores/"
	success_message = "El proveedor fue creado con exito."

class ProveedoresBorrarView(DeleteView):
	model = Proveedor
	success_url = "/proveedores/"
	template_name = "proveedores_app/proveedores_confirm_delete.html"
	success_message = "El proveedor fue borrado con exito."

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(ProveedoresBorrarView, self).delete(request, *args, **kwargs)

	def get_object(self):
		return get_object_or_404(Proveedor, pk=Proveedor.objects.filter(codigo=self.kwargs["codigo"]))

class ProveedoresDetalleView(DetailView):
	model = Proveedor
	template_name = "proveedores_app/detail.html"

	def get_object(self):
		return get_object_or_404(Proveedor, pk=Proveedor.objects.filter(codigo=self.kwargs["codigo"]))

class ProveedoresEditarView(SuccessMessageMixin, UpdateView):
    model = Proveedor
    fields = ['descripcion']
    template_name = "proveedores_app/proveedores_update_form.html"
    success_url = "/proveedores/"
    success_message = "El proveedor fue editado satisfactoriamente."   

    def get_object(self):
        return get_object_or_404(Proveedor, pk=Proveedor.objects.filter(codigo=self.kwargs["codigo"]))

class ProveedoresSearchView(ListView):
    model = Proveedor
    template_name = "proveedores_app/search_results.html"
    context_object_name = "found_entries"

    def get_queryset(self):
        found_entries = ""
        query_string = ""
        entry_query = ""
        queryset = super(ProveedoresSearchView, self).get_queryset()

        if ('q' in self.request.GET) and self.request.GET['q'].strip():
        
            query_string = self.request.GET['q']
            entry_query = get_query(query_string, ['descripcion', 'codigo'])
            found_entries = Proveedor.objects.filter(entry_query).order_by("descripcion")

        if ("ordering" in self.request.GET) and ("order_by" in self.request.GET) and (self.request.GET["q"] != ""):
            #ya estando los dos, se desarrolla la logica.
            campo = self.request.GET["order_by"]
            sentido = self.request.GET["ordering"]
            #se le asigna el valor a cada una

            if (sentido == "asc"):
                found_entries = Proveedor.objects.filter(entry_query).order_by(campo)

            else:
                found_entries = Proveedor.objects.filter(entry_query).order_by("-" + campo)


        queryset = found_entries
        return queryset

def handle(request, codigo):
    if request.method == "POST":

        if "borrar" in request.POST:
            return HttpResponseRedirect("/proveedores/"+codigo+"/borrar")

        if "editar" in request.POST:
            return HttpResponseRedirect("/proveedores/"+codigo+"/editar")

    else:
        raise Http404("Esta pagina no existe.")

