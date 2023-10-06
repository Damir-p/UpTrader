from django.shortcuts import render
from .models import MenuItem

def page(request):
    menu_items = MenuItem.objects.all()
    context = {
        'menu_items': menu_items,
    }
    return render(request, 'base.html', context)
