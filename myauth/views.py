from django.shortcuts import render
from .forms import regForm, logForm
from .models import User
from django.contrib import messages
from django.shortcuts import redirect

def login(request):
    if request.method == 'POST':
        form = logForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            userFound = list(User.objects.filter(login = login, password = password))    
            if userFound:
                messages.info(request, 'Неправильный логин или пароль!')
            else:
                return redirect('/main')
    
    context = {
        'logForm': logForm
    }
    return render(request, 'login.html', context)

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
