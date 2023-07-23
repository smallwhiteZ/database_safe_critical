from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('scenes/', views.members, name='members'),
    path('scenes/details/<int:id>', views.details, name='details'),
    path('reports/',views.all_reports,name='all_reports'),
    path('reports/<int:id>',views.report_details, name='reports'),
    path('reports/report_details/<int:id>',views.reports, name='report_details'),
]