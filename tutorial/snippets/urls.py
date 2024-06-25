from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetListMixin.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('employees/', views.employee_list),
    path('employees/<int:pk>/', views.employee_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)