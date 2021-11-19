from django.urls import path

from .views import HomePageView, AboutPageView,DiscoverPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('discover/', DiscoverPageView.as_view(), name='discover'),
]
