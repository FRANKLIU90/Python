from django.shortcuts import render


def home(request):
    return render(request, 'miguel/home.html')
