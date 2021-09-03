from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import RegisterForm
from .models import Classes


# from django.contrib.auth.decorators import user_passes_test


class IndexView(generic.ListView):
    template_name = 'education/index.html'
    context_object_name = 'class_list'

    def get_queryset(self):
        # return Classes.objects.order_by('class_name')[:10]
        return Classes.objects.filter(status=True)


class DetailView(generic.DetailView):
    model = Classes
    template_name = 'education/detail.html'
    context_object_name = 'Classes'


def register_form_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return HttpResponse('Form has been submitted successfully')
    else:
        form = RegisterForm()

    return render(request, 'education/register-form.html', context={
        'form': form
    })

# def is_teacher(user):
#     return user.groups.filter(name='Teacher').exists()
#
#
# @user_passes_test(is_teacher)
# def teacher_view(request):
#     pass
#
#
# def is_student(user):
#     return user.groups.filter(name='Student').exists()
#
#
# @user_passes_test(is_student)
# def student_view(request):
#     pass
#
#
# def is_staff(user):
#     return user.groups.filter(name='Staff').exists()
#
#
# @user_passes_test(is_staff)
# def staff_view(request):
#     pass
