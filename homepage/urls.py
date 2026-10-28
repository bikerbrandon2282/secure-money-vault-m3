from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('budget_overview/', views.budget_overview, name='budget_overview'),
    path('transactions/', views.transactions, name='transactions'),
    path('transactions/delete_transaction/<int:transactionId>',
         views.delete_transaction, name='delete_transaction'),
    path('reports/', views.reports, name='reports'),
    path('account/', views.account, name='account'),
    path('account/change_currency', views.change_currency, name='change_currency'),
    path('account/delete/', views.delete_user, name='delete_user'),
]