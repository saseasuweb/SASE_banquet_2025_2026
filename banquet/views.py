from django.shortcuts import render


def index(request):
    return render(request, 'banquet/index.html')

def details(request):
    return render(request, 'banquet/details.html')
