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
    if request.method == 'POST':
        form = create(request.POST)
        if form.is_valid():
            newDeal= User.objects.get(login=request.session['username'])
            form.save()
            return redirect('/main')
    
    user = User.objects.get(login=request.session['username']) 
    context = {
        "image": user.image,
        'username': request.session['username'],
        'createForm': create
    }
    return render(request, 'create.html', context)

def detail(request, id):
    getDeal = Deal.objects.get(id=id)
    user = User.objects.get(login=request.session['username']) 
    context = {
        "deal": getDeal,
        "image": user.image,
        'username': request.session['username']
    }
    return render(request, 'detail.html', context)