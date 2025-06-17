from django.urls import path
from menu import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.home, name='categories'),

    path('categories/electronics/', views.home, name='electronics'),
    path('categories/electronics/smartphones/', views.home, name='smartphones'),
    path('categories/electronics/laptops/', views.home, name='laptops'),

    path('categories/clothing/', views.home, name='clothing'),
    path('categories/clothing/men/', views.home, name='men_clothing'),
    path('categories/clothing/women/', views.home, name='women_clothing'),

    path('about/', views.home, name='about'),
    path('contacts/', views.home, name='contacts'),
]