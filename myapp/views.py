from django.shortcuts import render
from django.utils import timezone
from .models import InventoryItem

def home(request):
    # Get current date and time
    current_time = timezone.now()
    
    # Get inventory items
    inventory_items = InventoryItem.objects.all()
    
    context = {
        'current_time': current_time,
        'inventory_items': inventory_items,
        'inventory_count': inventory_items.count(),
    }
    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html')