from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from common.models import Course, Student, Address
from .forms import CourseForm, StudentForm, AddressForm

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
        kwargs['courses'] = Course.objects.all()
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


class AddAddressView(SuccessMessageMixin, FormView):
    template_name = 'front/address-add.html'
    form_class = AddressForm

    def get(self, request, *args, **kwargs):
        self.student_id = kwargs.get('student_id', None)
        return super(AddAddressView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.student_id = kwargs.get('student_id', None)
        return super(AddAddressView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['student_id'] = self.student_id
        student = Student.objects.get(id=self.student_id)
        kwargs['student'] = student
        return super(AddAddressView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.success_url = reverse_lazy(
            'front:student-edit',
            kwargs={'pk': self.student_id}
        )
        form.save()
        return super(AddAddressView, self).form_valid(form)


class AddressDeleteView(SuccessMessageMixin, DeleteView):
    model = Address

    def delete(self, request, *args, **kwargs):
        self.student_id = kwargs.get('student_id', None)
        self.success_url = reverse_lazy(
            'front:student-edit',
            kwargs={'pk': self.student_id}
        )
        messages.success(
            request,
            'Address was deleted successfully'
        )
        return super(AddressDeleteView, self).delete(request, *args, **kwargs)


class CourseLinkView(SuccessMessageMixin, TemplateView):
    template_name = 'front/course-link.html'
    
    def get(self, request, *args, **kwargs):
        student_id = kwargs.get('student_id', None)
        context = self.get_context_data(**kwargs)
        courses = Course.objects.all()
        student = Student.objects.get(id=student_id)
        context['student'] = student
        context['courses'] = courses
        context['student_id'] = student_id
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        course_part = 'curse-check-'
        student_id = kwargs.get('student_id', None)
        student = Student.objects.get(id=student_id)
        for value in request.POST.items():
            if course_part in value[0]:
                student.courses.add(Course.objects.get(id=value[0].replace(course_part, '')))
        student.save()
        self.success_url = reverse_lazy('front:student-edit', kwargs={'pk': student_id})
        messages.success(
            request,
            'Courses was linked successfully'
        )
        context = self.get_context_data(**kwargs)
        context['student_id'] = student_id
        return redirect(self.success_url, context)


class CourseUnlinkView(SuccessMessageMixin, TemplateView):
    template_name = 'common/course_confirm_unlink.html'

    def get(self, request, *args, **kwargs):
        student_id = kwargs.get('student_id', None)
        pk = kwargs.get('pk', None)
        course = Course.objects.get(id=pk)
        context = self.get_context_data(**kwargs)
        context['student_id'] = student_id
        context['object'] = course
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        course_part = 'curse-check-'
        student_id = kwargs.get('student_id', None)
        pk = kwargs.get('pk', None)
        student = Student.objects.get(id=student_id)
        student.courses.remove(Course.objects.get(id=pk))
        student.save()
        self.success_url = reverse_lazy('front:student-edit', kwargs={'pk': student_id})
        messages.success(
            request,
            'Courses was unlinked successfully'
        )
        context = self.get_context_data(**kwargs)
        context['student_id'] = student_id
        return redirect(self.success_url, context)
