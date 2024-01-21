from django.contrib import admin
from django.urls import path
from .views import account, expenses

urlpatterns = [

    path('', account, name='profile'),
    path('expense_summary/', expenses, name='expense'),

]
