from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import RegisterForm
from .models import Classes


class IndexView(generic.ListView):
    template_name = 'education/index.html'
    context_object_name = 'class_list'

    def get_queryset(self):
        return Classes.objects.order_by('class_name')[:10]


class DetailView(generic.DetailView):
    model = Classes
    template_name = 'education/detail.html'
    context_object_name = 'sp'


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
