from django.shortcuts import render,HttpResponse

# Create your views here.
def suggestions(request):
    return render(request,"suggestions.html")
