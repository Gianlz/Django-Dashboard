from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {'content': 'Gabriel'})

def configurations(request):
    return render(request, 'configurations.html')