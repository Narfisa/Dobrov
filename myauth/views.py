from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'reg.html')
