from django.utils import timezone

from django.contrib import messages
from django.shortcuts import render
from .models import transaction
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

def transactions(request):
    transaction_form = TransactionForm(request.POST)
    if request.method == 'POST':
        if transaction_form.is_valid():
            form = transaction_form.save(commit=False)
            if transaction_form.date == None:
                form.date = timezone.now()
            form.save()
            messages.success(request, 'Transaction added successfully!')
    transaction_form = TransactionForm()  # Reset the form after saving
    return render(request, 'transactions.html', {'transaction_form': transaction_form})

def reports(request):
    return render (request, 'reports.html')

def account(request):
    return render (request, 'account.html')

