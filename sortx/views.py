from django.shortcuts import HttpResponse, render
from django.http import JsonResponse

from .main import run_merge_excel
from .forms import SortxForm

# Create your views here.


def home(request):
    return render(request, "home.html")


def sortx(request):
    if request.method == "POST":
        form = SortxForm(request.POST)
        if form.is_valid():
            config_path = form.cleaned_data["config_path"]
            xl_folder_path = form.cleaned_data["xl_folder_path"]
            doc_folder_path = form.cleaned_data["doc_folder_path"]

            paths = {"config_path": config_path, "xl_folder_path": xl_folder_path, "doc_folder_path": doc_folder_path}

            run_merge_excel(paths)

    else:
        form = SortxForm()
    return render(request, "sortx.html", {"form": form})

