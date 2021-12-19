from django.urls import path

from . import views

urlpatterns = [
    path('view-article/', views.index, name='index'),
    path('create-author/', views.create_author, name='index'),
]