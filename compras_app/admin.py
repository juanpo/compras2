from django.contrib import admin
from .models import Producto, Orden, Proveedor




class ProductoAdmin(admin.ModelAdmin):
    fieldsets = [
	    ("Codigo", {"fields": ["codigo"]}),
		("Descripcion", {"fields": ["descripcion"]}),
    ]
    list_display = ("codigo", "descripcion")
    list_per_page = 700

	

class ProductoInline(admin.StackedInline):
    model = Producto
    extra = 1

	
class OrdenAdmin(admin.ModelAdmin):
    search_fields = ["proveedor__nombre", "productos__descripcion"]
    list_filter = ["proveedor__nombre"]
    list_display = ["__str__", "proveedor", "fecha"]
    inlines = [ProductoInline]
	

	

class ProveedorAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Codigo", {"fields": ["codigo"]}),
        ("nombre", {"fields": ["nombre"]}),
    ]

	

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(Proveedor, ProveedorAdmin)

