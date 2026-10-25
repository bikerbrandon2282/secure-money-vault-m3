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
    return render (request, 'budget_overview.html')

def add_transaction(request):
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
    return render (request, 'reports.html')

def account(request):
    return render (request, 'account.html')

