from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def index(request):
    return render (request, 'base.html')

def budget_overview(request):
    return render (request, 'budget_overview.html')

def transactions(request):
    return render (request, 'transactions.html')

def reports(request):
    return render (request, 'reports.html')

def account(request):
    return render (request, 'account.html')