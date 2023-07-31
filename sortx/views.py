from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>SortX</h1>")

def home(request):
    return render(request, "home.html")