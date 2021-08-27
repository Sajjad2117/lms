from django.db import models


# Create your models here.

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.faculty_name}'


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)
    faculty_name = models.ManyToManyField(Faculty)

    def __str__(self):
        return f'{self.teacher_name}'


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    teacher_name = models.ManyToManyField(Teacher)

    def __str__(self):
        return f'{self.course_name}'


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    major = models.CharField(max_length=200, default="Photonics")
    course = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.student_name}'


class Classes(models.Model):
    class_name = models.CharField(max_length=150)
    faculty_name = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    course = models.ManyToManyField(Course)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.class_name} '
