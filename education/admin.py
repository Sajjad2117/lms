from django.contrib import admin

from .models import Teacher, Student, Course, Faculty, Classes, University, Major, Staff

# Register your models here.
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Major)
admin.site.register(Classes)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Staff)
# admin.site.register(User)


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     pass
