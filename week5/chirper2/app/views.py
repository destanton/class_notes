from django.shortcuts import render
from app.models import Chirp
from app.forms import ChirpForm


def index_view(request):
    print(request.POST)
    if request.POST:
        instance = ChirpForm(request.POST)
        if instance.is_valid():
            instance.save()  # converts from form data and makes and instance in the database.
    context = {
        "form": ChirpForm(),
        "all_chirps": Chirp.objects.all().order_by("-created")

    }
    return render(request, "index.html", context)


def about_view(request):
    print(request.GET)
    message = request.GET.get("message", "")
    voice = request.POST.get("voice", "")
    print(request.POST)
    return render(request, "about.html")
