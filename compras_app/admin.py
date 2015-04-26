from django.contrib import admin
from .models import Producto




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

	

admin.site.register(Producto, ProductoAdmin)


