from datetime import datetime, timedelta
from django.test import TestCase
from django.urls import reverse

from common.models import Course

# Create your tests here.
class TestFrontViews(TestCase):

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

    def test_homeview(self):
        url = reverse('front:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_courselistview(self):
        url = reverse('front:course-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_coursecreateview(self):
        url = reverse('front:course-add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_courseupdateview(self):
        course = self.create_course()
        url = reverse('front:course-edit', kwargs={'pk':course.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_coursedeleteview(self):
        course = self.create_course()
        url = reverse('front:course-delete', kwargs={'pk':course.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)