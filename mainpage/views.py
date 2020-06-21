from django.shortcuts import render
from .forms import create
from .models import Deal
from myauth.models import User
from django.contrib import messages
from django.shortcuts import redirect

def main(request):
    items = list(Deal.objects.all())
    user = User.objects.get(login=request.session['username'])
    context = {
        'items': items,
        "image": user.image,
        'username': request.session['username']
    }
    return render(request, 'mainpage.html', context)

def add(request):
    pass
    # if request.method == 'POST':
    #     form = regForm(request.POST)
    #     if form.is_valid():
    #         login = form.cleaned_data['login']
    #         email = form.cleaned_data['email']
    #         loginFound = list(User.objects.filter(login = login))            
    #         emailFound = list(User.objects.filter(email = email))
    #         if loginFound or emailFound:
    #             messages.info(request, 'Такой логин или email уже существует!')
    #         else:
    #             form.save()
    #             return redirect('/main')
    
    # context = {
    #     'regForm': regForm
    # }
    # return render(request, 'reg.html', context)

def detail(request, id):
    getDeal = Deal.objects.get(id=id)
    user = User.objects.get(login=request.session['username']) 
    context = {
        "deal": getDeal,
        "image": user.image,
        'username': request.session['username']
    }
    return render(request, 'detail.html', context)