from django.shortcuts import render
from app.models import Chirp


def index_view(request):
    print(request.POST)
    if request.POST:
        chirp_body = request.POST["chirp_body"]
        if chirp_body != "" and len(chirp_body) <= 140:
            Chirp.objects.create(body=chirp_body)
    context = {
        "all_chirps": Chirp.objects.all().order_by("-created")

    }
    return render(request, "index.html", context)


def about_view(request):
    return render(request, "about.html")
