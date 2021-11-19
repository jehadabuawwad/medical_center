from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class DiscoverPageView(TemplateView):
    template_name = 'pages/discover.html'