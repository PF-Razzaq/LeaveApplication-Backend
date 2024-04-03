from django.contrib import admin
from .models import Employee,ApplyForLeave,LeaveTable

admin.site.register(Employee)
admin.site.register(ApplyForLeave)
admin.site.register(LeaveTable)
# Register your models here.
