from django.shortcuts import render


def index(request):
    """The main page for the accounts application"""
    return render(request, 'accounts/index.html')
