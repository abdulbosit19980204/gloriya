from django.shortcuts import render


# Create your views here.

def dashboard_view(request):
    return render(request, 'dashboard.html')


def login_view(request):
    return render(request, 'login.html')


def logout_view(request):
    return render(request, '')
