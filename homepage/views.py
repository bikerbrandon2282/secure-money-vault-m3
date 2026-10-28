from django.utils import timezone

from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Transaction, Profile
from .forms import TransactionForm
# from django.http import HttpResponse
# Create your views here.


'''
These are functions to render the different pages of the website. 
Each function corresponds to a specific page and uses the render function 
to return the appropriate HTML template.
'''
def index(request):
    '''
    This Function just displays the home page for all users
    '''
    return render (request, 'base.html')


def budget_overview(request):
    '''
    This is a Function to render the budget_overview page,
    However this has not currently been implemented and will render a basic 404 page.
    '''
    return render (request, '404.html') # Eventually renders to budget_overview.html


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
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render (request, 'account.html', {'profile': profile})


def change_currency(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":

        profile.currency = int(
            request.POST.get("currency")
        )

        profile.save()

    return redirect("account")

def delete_user(request):
    '''
    This is the function to delete a user account and associated transactions 
    '''
    user = request.user

    logout(request)      # Remove session
    user.delete()        # Delete user
    return redirect("home")


def transactions(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    transaction_id = request.POST.get('transaction_id')

    if request.method == 'POST':
        if transaction_id:
            transaction = get_object_or_404(
                Transaction,
                id=transaction_id,
                user=request.user
            )
        
            transaction_form = TransactionForm(
                request.POST,
                instance=transaction
            )
        else:
            transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            form = transaction_form.save(commit=False)
            form.user = request.user  # Set the user to the currently logged-in user
            form.save()
            if transaction_id:
                messages.success(request, 'Transaction Updated successfully!')
            else:
                messages.success(request, 'Transaction Added successfully!')
    transaction_form = TransactionForm()  # Reset the form after saving
    transactions = Transaction.objects.filter(user=request.user)

    total_income = (
        transactions.filter(type='1') # Type 1 is Income key in database
        .aggregate(Sum('amount'))['amount__sum']
        or 0
    )

    total_expenses = (
        transactions.filter(type='2')  # Type 2 is Expense key in database
        .aggregate(Sum('amount'))['amount__sum']
        or 0
    )

    currency_symbol = profile.currency_symbol


    balance = total_income - total_expenses

    context = {
        'transaction_form': transaction_form,
        'transactions': transactions,
        'currency_symbol': currency_symbol,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
        'transaction_count': transactions.count(),
    }

    return render(request, 'transactions.html', context)


def delete_transaction(request, transactionId):
    """
    view to delete transactions
    """
    queryset = Transaction.objects.filter(user=request.user)
    transaction = get_object_or_404(queryset, id=transactionId)

    if transaction.user == request.user:
        transaction.delete()
        messages.add_message(request, messages.SUCCESS, 'Transaction deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'There was a problem deleting your Transaction')

    return redirect('transactions')