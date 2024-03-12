from django.urls import path, re_path
from .views import EmployeeListCreateView,ApplyForLeaveListCreateView,EmployeeDetailView
from . import views

urlpatterns = [
    # for employee
    path('api/employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('api/login/', views.login_view, name='login-view'),
    path('api/logout/', views.logout_view, name='logout-view'),
    path('api/employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    re_path(r'^api/employees/$', views.employees_list, name='employees-list'),
    re_path(r'^api/employees/([0-9]+)$', views.employees_detail, name='employees-detail'),
    
    # for apply leave
    path('api/leave/', ApplyForLeaveListCreateView.as_view(), name='apply-list-create'),
    re_path(r'^api/leave/$', views.apply_leave_list, name='apply_leave_list'),
    re_path(r'^api/leave/<int:employee_id>/', views.apply_leave_list, name='apply_leave_list-employee'),
    re_path(r'^api/leave/([0-9]+)$', views.apply_leave_detail, name='apply_leave_detail'),

]