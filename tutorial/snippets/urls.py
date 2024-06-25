from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('employees/', views.employee_list),
    path('employees/<int:pk>/', views.employee_detail),
]