from django.shortcuts import render
from .forms import create
from .models import Deal
from myauth.models import User
from django.contrib import messages
from django.shortcuts import redirect


def handle_uploaded_file(f):
    destination = open('addfile', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()



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
        form = create(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            #handle_uploaded_file(request.FILES.get('image'))
            form.save()
            newDeal= list(Deal.objects.all())[-1]
            return redirect('/main/detail/'+str(newDeal.id))
    else:
        form = create()

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