from django.http import JsonResponse
from django.shortcuts import HttpResponse, render


# Create your views here.
def suggestions(request):
    return render(request, "suggestions.html")


def set_progress(request):
    # Initialize progress in the session
    request.session["progress"] = 0
    return JsonResponse({"progress": 0})


def update_progress(request):
    # Get current progress from the session or set to 0 if not present
    progress = request.session.get("progress", 0)

    # Calculate the new progress
    new_progress = min(progress + 1, 1000)  # Limit progress to 1000 (range(1000))

    # Update the progress in the session
    request.session["progress"] = new_progress

    # Return the new progress as a percentage
    return JsonResponse({"progress": (new_progress / 1000) * 100})
