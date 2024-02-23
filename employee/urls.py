from django.urls import path, re_path
from .views import EmployeeListCreateView
from . import views

urlpatterns = [
    path('api/employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    re_path(r'^api/employees/$', views.employees_list, name='employees-list'),
    re_path(r'^api/employees/(?P<pk>[0-9]+)$', views.employees_detail, name='employees-detail'),
]