from django import forms 

from common.models import Course, Student, Address


class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ('code', 'name', 'init_date', 'end_date')


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('name', 'last_name', 'birthdate', 'gender')


class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ('location', 'addr_type', 'student')
