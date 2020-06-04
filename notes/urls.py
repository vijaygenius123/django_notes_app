from django.urls import path

from .views import list, create

urlpatterns =[
    path('',list, name='list'),
    path('create/',create, name='create')
]