from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator,InvalidPage, EmptyPage
from django.db.models import Q
from .models import *

# Create your views here.
def index(request,cslug=None):
    if cslug != None:
        cpro = get_object_or_404(categ, slug = cslug)
        pag = product.objects.all().filter(category=cpro)

    else:
        obj = product.objects.all()
        var = Paginator(obj, 4)
        pgnum = int(request.GET.get('page', 1))
        try:
            pag = var.page(pgnum)
        except (InvalidPage, EmptyPage):
            pag = var.page(var.num_pages)

    obj2 = categ.objects.all()
    return render(request, 'index.html', {'i': pag, 'j': obj2})

def search(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        eco = product.objects.filter(Q(name__icontains=query) | Q(price__icontains=query))
        obj2 = categ.objects.all()
    return render(request, 'search.html', {'var':eco,'j':obj2})
def details(request,cslug,pslug):
    deta=product.objects.get(category__slug = cslug, slug = pslug)

    return render(request,'product-single.html',{'c':deta})

def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def home(request,cslug=None):
    if cslug != None:
        cpro = get_object_or_404(categ, slug = cslug)
        pag = product.objects.all().filter(category=cpro)

    else:
        obj = product.objects.all()
        var = Paginator(obj, 4)
        pgnum = int(request.GET.get('page', 1))
        try:
            pag = var.page(pgnum)
        except (InvalidPage, EmptyPage):
            pag = var.page(var.num_pages)

    obj2 = categ.objects.all()
    return render(request, 'home.html', {'i': pag, 'j': obj2})
