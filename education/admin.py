from django.contrib import admin

from .models import Teacher, Student, Course, Faculty, Classes

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Classes)


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     pass
