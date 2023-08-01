from django.shortcuts import render, HttpResponse

# Create your views here.
def calculationsheets(request):
    return render(request, "calculationsheets.html")