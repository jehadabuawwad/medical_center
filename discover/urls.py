from django.urls import path

from .views import (
                    discover_create_view,
                    )

urlpatterns = [
    path('create/',discover_create_view,name="create"),
]
