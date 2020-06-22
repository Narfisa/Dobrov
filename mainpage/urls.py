from django.urls import path

from .views import main, add, detail

urlpatterns = [
    path('', main),
    path('create/', add),
    path('detail/<int:id>', detail)
]
