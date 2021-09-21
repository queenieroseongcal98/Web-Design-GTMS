from django.urls import path, include
from . import views

urlpatterns = [
    path('homecarrier/', views.homecarrier, name='homecarrier'),
    path('transactions/', views.transactions, name='transactions'),
    path('feedback/', views.feedback, name='feedback'),
]