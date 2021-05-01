from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from common.models import Course, Student
from .forms import CourseForm, StudentForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'front/home.html'


class CourseListView(TemplateView):
    template_name = 'front/course-list.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        return self.render_to_response(context)


class CourseCreateView(SuccessMessageMixin, CreateView):
    template_name = 'front/course-add-edit.html'
    form_class = CourseForm
    success_url = reverse_lazy('front:course-add')
    success_message = 'Course was created succesfully'


class CourseUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'front/course-add-edit.html'
    form_class = CourseForm
    model = Course
    success_message = 'Course was updatd succesfully'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super(CourseUpdateView, self).get_context_data(**kwargs)
    
    def form_valid(self, form):
        self.success_url = reverse_lazy(
            'front:course-edit',
            kwargs={'pk': self.object.pk}
        )
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(SuccessMessageMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('front:course-list')

    def delete(self, request, *args, **kwargs):
        messages.success(
            request,
            'Course was deleted successfully'
        )
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)














class StudentListView(TemplateView):
    template_name = 'front/student-list.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        students = Student.objects.all()
        context['students'] = students
        return self.render_to_response(context)


class StudentCreateView(SuccessMessageMixin, CreateView):
    template_name = 'front/student-add-edit.html'
    form_class = StudentForm
    success_url = reverse_lazy('front:student-add')
    success_message = 'Student was created succesfully'


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'front/student-add-edit.html'
    form_class = StudentForm
    model = Student
    success_message = 'Student was updatd succesfully'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super(StudentUpdateView, self).get_context_data(**kwargs)
    
    def form_valid(self, form):
        self.success_url = reverse_lazy(
            'front:student-edit',
            kwargs={'pk': self.object.pk}
        )
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('front:student-list')

    def delete(self, request, *args, **kwargs):
        messages.success(
            request,
            'Student was deleted successfully'
        )
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
