from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('habits/', views.list_habits, name='list-habits'),
]
