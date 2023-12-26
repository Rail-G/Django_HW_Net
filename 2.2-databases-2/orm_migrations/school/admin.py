from django.contrib import admin

from .models import StudTeach, Student, Teacher

class StudInline(admin.TabularInline):
    model = StudTeach

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

