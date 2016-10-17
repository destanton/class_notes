from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Chirp, Vote
from app.forms import ChirpForm


# def index_view(request):
#     print(request.POST)
#     if request.POST:
#         instance = ChirpForm(request.POST)
#         if instance.is_valid():
#             instance.save()  # converts from form data and makes and instance in the database.
#     context = {
#         "form": ChirpForm(),
#         "all_chirps": Chirp.objects.all().order_by("-created")
#     }
#     return render(request, "index.html", context)


def about_view(request):
    print(request.GET)
    message = request.GET.get("message", "")
    voice = request.POST.get("voice", "")
    print(request.POST)
    return render(request, "about.html")


class ChirpView(ListView):  # class name is what's called in urls.py/inheriting View from django.views

    template_name = "chirps.html"
    model = Chirp

    # def get_context_data(self):
    #     context = {
    #      "all_chirps": Chirp.objects.all()
    #     }
    #     return context

    # def get(self, request):
    #     return render(request, "chirps.html")
    # def post(self, request):
    #     return render(request, "chirps.html")


class ChirpDetailView(DetailView):
    model = Chirp


class ChirpCreateView(CreateView):
    model = Chirp
    success_url = "/"
    fields = ('body',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class ChirpUpdateView(UpdateView):
    model = Chirp
    success_url = "/"
    fields = ('body',)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"  # show reverse lazy
    # fields = ('username', 'password')


class ChirpVoteView(CreateView):
    model = Vote
    success_url = "/"
    fields = ('value',)

    def form_valid(self, form):
        try:
            Vote.objects.get(user=self.request.user, chirp_id=self.kwargs['pk']).delete()
        except Vote.DoesNotExist:
            pass
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.chirp = Chirp.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
