from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html', {
        'brand': 'Library Now',
        'whatwedo': 'Here you can find and lend your favorite books, enjoy!',
    })

def contact_view(request):
    return render(request, 'contact.html')