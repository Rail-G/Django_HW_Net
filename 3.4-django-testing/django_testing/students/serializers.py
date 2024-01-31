from rest_framework import serializers

from students.models import Course
from django_testing.settings import MAX_STUDENTS_PER_COURSE

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, attrs):
        if len(attrs['students']) > MAX_STUDENTS_PER_COURSE:
            raise serializers.ValidationError('Больше 20 студентов в одном курсе')
        return attrs