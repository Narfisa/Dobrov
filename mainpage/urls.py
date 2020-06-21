from django.urls import path

from .views import main, create, detail

urlpatterns = [
    path('', main),
    path('create/', create),
    path('detail/<int:id>', detail)
]
