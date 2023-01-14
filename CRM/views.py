from django.shortcuts import render, reverse
from django.views.generic import CreateView

from Leads.forms import NewUserCreationForm


def landing_page(request):
    return render(request, "landing.html")


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserCreationForm

    def get_success_url(self):
        return reverse("login")
