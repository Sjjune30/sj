from django.shortcuts import render

from EcomApp.models import Product
from django.db.models import Q


# Create your views here.
def SearchResult(request):
    product = None
    Query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(name__contains=query)
        return render(request, 'search.html', {'query': query, 'products': products})
