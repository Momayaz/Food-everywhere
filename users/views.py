from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {userName}, you created account successfully.')
            return redirect('foods:homePage') 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form})