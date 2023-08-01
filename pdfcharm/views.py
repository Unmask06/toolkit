from django.shortcuts import render, HttpResponse

# Create your views here.

def pdfcharm(request):
    return render(request, "pdfcharm.html")