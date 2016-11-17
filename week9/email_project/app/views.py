from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["form"] = ContactForm()
        return context


class SendEmailView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy("index_view")  # used outside of a class method. Don't need to pass params

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
