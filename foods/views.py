from django.shortcuts import render
from .models import Data
# Create your views here.

def homePage(request):
    list_item = Data.objects.all()
    context = {
        'list_item':list_item,
    }
    return render(request,'index.html', context)
def detailsPage(request,food_id):
    item = Data.objects.get(pk=food_id)
    context = {
        'item':item,
    }
    return render(request, 'details.html', context)

def aboutPage(request):
    return render(request,'about.html')