from django.urls import path

from myauth.views import reg, login

urlpatterns = [
    path('login', login),
    path('reg', reg),
    path('', reg)
]
