from django.shortcuts import render

from django.shortcuts import render

from bs4 import BeautifulSoup
from django.http import HttpResponse

# Create your views here.


def studentInfo(request):
    return render(request, "pages/index.html")
