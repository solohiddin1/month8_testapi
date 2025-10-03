from django.urls import path
from .views import EmployeeView, StatisticsClient, StatisticsViews

urlpatterns = [
    path('statistics/client/<int:pk>/', StatisticsClient.as_view()),
    path('employee/statistics/', EmployeeView.as_view()),
    path("statistics/employee/<int:pk>/", StatisticsViews.as_view(), name="employee-statistics")

]
