from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return render(request, 'pages/contact.html')

# Create your views here.
