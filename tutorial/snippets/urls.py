from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('employees/', views.employee_list),
    path('employees/<int:pk>/', views.employee_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)