from django.views.generic import ListView
from django.shortcuts import render

from .models import StudTeach, Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.prefetch_related("teacher")
    context = {'object_list': object_list}
    return render(request, template, context)
