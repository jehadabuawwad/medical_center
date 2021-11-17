from django.urls import path

from .views import DiscoverView

urlpatterns = [
    path('', DiscoverView.as_view(), name='discover'),
]
