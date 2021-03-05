from django.shortcuts import render, redirect
from .models import Data
from .forms import ItemForm
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



def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('foods:homePage')

    return render(request, 'forms.html', {'form': form})

def update_item(request, id):
    item = Data.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('foods:homePage')

    return render(request, 'forms.html', {'item':item,'form':form})

def delete_item(request, id):
    item = Data.objects.get(id=id)

    if request.method == 'POST' :
        item.delete()
        return redirect('foods:homePage')

    return render(request, 'delete_item.html', {'item':item})

def aboutPage(request):
    return render(request,'about.html')

