from datetime import datetime, timedelta
from django.test import TestCase
from .models import Student, Course, Address

# Create your tests here.
class CommonModelTestCase(TestCase):

    def create_student(self):
        return Student.objects.create(
            name='Sergio',
            last_name='Ramos',
            birthdate=datetime.strptime('2000-01-01', '%Y-%m-%d').date(),
            gender=Student.MALE,
        )

    def create_course(self):
        return Course.objects.create(
            code='Mate-01',
            name='Matemáticas',
            init_date=datetime.today(),
            end_date=datetime.today() + timedelta(30),
        )

    def create_address(self):
        student = self.create_student()
        return Address.objects.create(
            location='F8WQ+VG Madrid, España',
            addr_type=Address.TEMPORAL,
            student=student
        )

    def test_student_model_str(self):
        student = self.create_student()
        full_name = '{} {}'.format(student.name, student.last_name)
        self.assertEqual(full_name, student.__str__())
    
    def test_course_model_str(self):
        course = self.create_course()
        course_name = '{}-{}'.format(course.code, course.name)
        self.assertEqual(course_name, course.__str__())

    def test_address_model_str(self):
        address = self.create_address()
        self.assertEqual(address.location, address.__str__())
