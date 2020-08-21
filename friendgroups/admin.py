from django.contrib import admin

# Register your models here.
from .models import Group, Person, Category, Meeting, Attendance


admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Meeting)
admin.site.register(Attendance)
