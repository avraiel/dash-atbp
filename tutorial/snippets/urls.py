from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

from snippets import gabriel

urlpatterns = [
    path('snippets/', views.SnippetListMixin.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('employees/', views.employee_list),
    path('employees/<int:pk>/', views.employee_detail),
    path('test/', views.gabriel, name="gabriel"),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('roles/', views.role_list),
    path('roles/<int:pk>/', views.role_detail, name="role_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)