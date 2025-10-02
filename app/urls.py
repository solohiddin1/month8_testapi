from django.urls import path
from .views import StatisticsViews

urlpatterns = [
    # path('get/<int:pk>/<int:year>', StatisticsViews.as_view())
    path("statistics/employee/<int:pk>/", StatisticsViews.as_view(), name="employee-statistics")

]
