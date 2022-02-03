from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class TodoTV(TemplateView):
    template_name = 'todo/todo_index.html'