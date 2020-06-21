from django.shortcuts import render
from .forms import create
from .models import Deal
from django.contrib import messages
from django.shortcuts import redirect

def main(request):
    items = list(Deal.objects.all())    
    return render(request, 'mainpage.html')

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
