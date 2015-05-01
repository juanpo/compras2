from django.shortcuts import render
from compras_app.models import Producto
from search_app.utils import get_query

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['descripcion', 'codigo'])
        
        found_entries = Producto.objects.filter(entry_query).order_by('descripcion')

    return render(request, 'search_app/search_results.html', {
		'query_string': query_string,
		'found_entries': found_entries
		})



