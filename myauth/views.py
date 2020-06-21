from django.shortcuts import render
from .forms import regForm
from .models import User
from django.contrib import messages
from django.shortcuts import redirect

def login(request):
    return render(request, 'login.html')

def reg(request):
    if request.method == 'POST':
        form = regForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            loginFound = list(User.objects.filter(login = login))            
            emailFound = list(User.objects.filter(email = email))
            if loginFound or emailFound:
                messages.info(request, 'Такой логин или email уже существует!')
            else:
                form.save()
                return redirect('/main')
    
    context = {
        'regForm': regForm
    }
    return render(request, 'reg.html', context)
