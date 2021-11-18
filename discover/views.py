from django.views.generic import ListView,CreateView
from .models import Malady


class DiscoverListView(ListView):
    template_name="pages/discover.html"
    model=Malady


class DiscoverCreateView(CreateView):
    template_name = "pages/discover.html"
    model = Malady
    fields = ["name", "email", "mobile","paitent","age","bmi","avg_glucose_level","gender","ever_married","hypertension","work"]
    context_object_name = "create"