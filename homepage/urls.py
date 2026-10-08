from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('budget_overview/', views.budget_overview, name='budget_overview'),
    path('transactions/', views.transactions, name='transactions'),
    path('reports/', views.reports, name='reports'),
    path('account/', views.account, name='account'),
]