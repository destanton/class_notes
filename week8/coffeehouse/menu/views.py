from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework.generics import ListAPIView
from menu.models import Special
from django.urls import reverse_lazy
from menu.serializers import SpecialSerializer


class SpecialListView(ListView):
    model = Special


class SpecialCreateView(CreateView):
    model = Special
    fields = ('title', 'description', 'picture')
    success_url = reverse_lazy("special_list_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_user = self.request.user
        return super().form_valid(form)


class SpecialUpdateView(UpdateView):
    model = Special
    fields = ('title', 'description', 'picture')
    success_url = reverse_lazy("special_list_view")


class SpecialListAPIView(ListAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer

    # def get_queryset(self):
    #     import time
    #     time.sleep(1)
    #     return Special.objects.all()
