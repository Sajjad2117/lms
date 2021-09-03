from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import AbstractUser


# class MyUserManager(BaseUserManager):
#     def create_user(self, phone, first_name, last_name, image=None, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not phone:
#             raise ValueError('Users must have an phonenumber')
#
#         user = self.model(
#             phone=phone,
#             first_name=first_name,
#             last_name=last_name,
#             image=image,
#
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, phone, first_name, last_name, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             phone=phone,
#             first_name=first_name,
#             last_name=last_name,
#             password=password,
#         )
#
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
#
# class User(AbstractUser):
#     phone = models.CharField(max_length=50, unique=True, blank=False, null=False)
#     image = models.ImageField(blank=True, null=True)
#     username = None
#     email = None
#     user_ptr = None
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#
#     # is_teacher = models.BooleanField(default=False)
#     # is_student = models.BooleanField(default=False)
#     # is_staff = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'phone'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     objects = MyUserManager()
#
#     def __str__(self):
#         return self.first_name
#

class University(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.faculty_name}'


class Major(models.Model):
    major_name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.major_name}'


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.course_name}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=15, null=True, default=' ')
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    course = models.ManyToManyField(Course)

    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} -- {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    # image = models.ImageField(null=True, upload_to=get_path, default='profile.png')
    student_id = models.CharField(max_length=15, null=True, default=' ')
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} -- {self.last_name}'


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} -- {self.last_name}'


class Classes(models.Model):
    class_name = models.CharField(max_length=150)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField(Student)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.class_name}'
