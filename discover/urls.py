from django.urls import path

from .views import (
                    discover_create_view,
                    ResultListView,
                    ResultDetailView

                    )

urlpatterns = [
    path('create/',discover_create_view,name="discover_create"),
    path('result/',ResultListView.as_view(),name="result_list"),
    path ('result/<int:pk>/',ResultDetailView.as_view(),name="result_detail"),
    
]
