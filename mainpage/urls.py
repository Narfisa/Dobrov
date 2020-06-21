from django.urls import path

from .views import main, create

urlpatterns = [
    path('', main),
    path('/create', create)
]
