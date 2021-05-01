from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    init_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return '{}-{}'.format(self.code, self.name)


class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, MALE),
        (FEMALE, FEMALE)
    ]

    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    courses = models.ManyToManyField(Course, verbose_name="courses")

    def __str__(self):
        return '{} {}'.format(self.name, self.last_name)


class Address(models.Model):
    WORK = 'W'
    HOME = 'H'
    TEMPORAL = 'T'
    ADDR_TYPE = [
        (WORK, 'WORK'), 
        (HOME, 'HOME'),
        (TEMPORAL, 'TEMPORAL')
    ]

    location = models.CharField(max_length=80)
    addr_type = models.CharField(max_length=1, choices=ADDR_TYPE)
    student = models.ForeignKey(Student, verbose_name="student", on_delete=models.CASCADE)

    def __str__(self):
        return self.location