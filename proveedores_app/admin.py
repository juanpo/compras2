from django.contrib import admin
from .models import Proveedor




class ProveedorAdmin(admin.ModelAdmin):
    fieldsets = [
	    ("Codigo", {"fields": ["codigo"]}),
		("Descripcion", {"fields": ["descripcion"]}),
    ]
    list_display = ("codigo", "descripcion")

	
class ProveedorInline(admin.StackedInline):
    model = Proveedor
    extra = 1

	

admin.site.register(Proveedor, ProveedorAdmin)