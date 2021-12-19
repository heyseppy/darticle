from django.urls import path

from . import views

urlpatterns = [
    path('view-article/<int:pk>', views.view_article, name='index'),
    path('create-author/', views.create_author, name='index'),
]