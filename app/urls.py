from django.urls import path
from .views import EmployeeView, StatisticsViews

urlpatterns = [
    path('employee/statistics/<int:pk>/', EmployeeView.as_view()),
    path("statistics/employee/<int:pk>/", StatisticsViews.as_view(), name="employee-statistics")

]
