from django.contrib import admin

# Register your models here.
from .models import Group, Person, Category, Meeting, Attendance


class AttendanceInline(admin.TabularInline):
    model = Attendance

class MeetingAdmin(admin.ModelAdmin):
    inlines = [
        AttendanceInline,
    ]


admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Attendance)
