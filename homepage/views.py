from django.utils import timezone

from django.contrib import messages
from django.shortcuts import render
from .models import Transaction
from .forms import TransactionForm
# from django.http import HttpResponse
# Create your views here.


'''
These are functions to render the different pages of the website. 
Each function corresponds to a specific page and uses the render function 
to return the appropriate HTML template.
'''
def index(request):
    return render (request, 'base.html')


def budget_overview(request):
    '''
    This is a Function to render the budget_overview page,
    However this has not currently been implemented and will render a basic 404 page.
    '''
    return render (request, '404.html') # Eventually renders to budget_overview.html


def add_transaction(request):
    '''
    This is the function for adding a transaction to the database
    '''
    transaction_form = TransactionForm(request.POST)
    if request.method == 'POST':
        if transaction_form.is_valid():
            form = transaction_form.save(commit=False)
            form.user = request.user  # Set the user to the currently logged-in user
            form.save()
            messages.success(request, 'Transaction added successfully!')
    transaction_form = TransactionForm()  # Reset the form after saving
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transactions.html', {'transaction_form': transaction_form, 'transactions': transactions})



def reports(request):
    '''
    This is a Function to render the reports page,
    However this has not currently been implemented and will render a basic 404 page.
    '''
    return render (request, '404.html') # Eventually will be rendered to reports.html


def account(request):
    '''
    This is the function to render the Account page
    '''
    return render (request, 'account.html')

