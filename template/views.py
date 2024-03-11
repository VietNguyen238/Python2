from django.shortcuts import render
from .models import NhatKy
from django.shortcuts import render
# Create your views here.
def blog(request):
    Data = {"Posts": NhatKy.objects.all().order_by("-date")}
    return render(request, "blog.html", Data)


def post(request, id):
    post = NhatKy.objects.get(id=id)
    return render(request, "post.html", {"post": post})
