from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    models = models.School
    template_name = 'basic_app/school_detail.html'
