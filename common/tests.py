from datetime import datetime, timedelta
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

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


class CommonSerializersTestCase(APITestCase):

    def create_student(self):
        return Student.objects.create(
            name='Sergio',
            last_name='Ramos',
            birthdate=datetime.strptime('2000-01-01', '%Y-%m-%d').date(),
            gender=Student.MALE,
        )

    def test_create_student(self):
        name = 'Maria'
        data = {'name': name, 'last_name': 'Serrano', 'birthdate': '1998-01-05', 'gender': 'F'}
        response = self.client.post('/common/student/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().name, name)

    def test_get_students(self):
        student = self.create_student()
        response = self.client.get('/common/student/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_update_student(self):
        student = self.create_student()
        name = 'Otro'
        data = {
            'id': student.id,
            'name': name,
            'last_name': student.last_name,
            'birthdate': student.birthdate,
            'gender': student.gender
        }
        response = self.client.put('/common/student/{}/'.format(student.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.get(id=student.id).name, name)

    def test_delete_student(self):
        student = self.create_student()
        response = self.client.delete('/common/student/{}/'.format(student.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Student.DoesNotExist):
            Student.objects.get(id=student.id)
