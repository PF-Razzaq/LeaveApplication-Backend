from django.urls import path, re_path
from .views import ApplyForLeaveListCreateView
from . import views

urlpatterns = [
    path('api/apply-leave/', ApplyForLeaveListCreateView.as_view(), name='apply-leave-list-create'),
    re_path(r'^api/apply-leave/$', views.apply_leave_list, name='apply-leaves-list'),
    re_path(r'^api/apply-leave/(?P<pk>[0-9]+)$', views.apply_leave_detail, name='apply-leave-detail'),
]