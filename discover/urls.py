from django.urls import path

from .views import (
                    DiscoverListView,
                    DiscoverCreateView,
                    )

urlpatterns = [
    path('', DiscoverListView.as_view(), name='discover'),
    path('create/',DiscoverCreateView.as_view(),name="create"),
]
