from django import forms 

from common.models import Course, Student


class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ('code', 'name', 'init_date', 'end_date')


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('name', 'last_name', 'birthdate', 'gender')
