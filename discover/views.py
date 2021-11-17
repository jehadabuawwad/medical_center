from django.shortcuts import render
from django.views.generic import ListView
from .models import Malady


class DiscoverView(ListView):
    template_name="pages/discover.html"
    model=Malady
