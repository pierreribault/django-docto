from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def account(request):
    return render(request, 'account.html')
