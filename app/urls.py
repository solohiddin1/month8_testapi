from django.urls import path
from .views import StatisticsViews

urlpatterns = [
    path('get/<int:pk>/<int:year>', StatisticsViews.as_view())
]
