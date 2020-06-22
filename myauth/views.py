from django.shortcuts import render
from .forms import regForm, logForm
from .models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def correctEmail(email):
    value = email
    try:
        validate_email(value)
    except ValidationError:
        return False
    else:
        return True


def login(request):
    if request.session.has_key('username'):
        return redirect('/main', {"username": request.session['username']})

    if request.method == 'POST':
        form = logForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            userFound = list(User.objects.filter(login = login, password = password))    
            if not userFound:
                messages.info(request, 'Неправильный логин или пароль!')
            else:
                request.session['username'] = login
                return redirect('/main')
    
    context = {
        'logForm': logForm
    }
    return render(request, 'login.html', context)

def reg(request):
    if request.session.has_key('username'):
        return redirect('/main', {"username": request.session['username']})

    if request.method == 'POST':
        form = regForm(request.POST)
        email = form.cleaned_data['email']
        if correctEmail(email):
            if form.is_valid():
                login = form.cleaned_data['login']
                loginFound = list(User.objects.filter(login = login))            
                emailFound = list(User.objects.filter(email = email))
                if loginFound or emailFound:
                    messages.info(request, 'Такой логин или email уже существует!')
                else:
                    form.save()
                    request.session['username'] = login
                    return redirect('/main')
        else:
            messages.info(request, 'Неккоректный email адрес')
        
    context = {
        'regForm': regForm
    }
    return render(request, 'reg.html', context)
