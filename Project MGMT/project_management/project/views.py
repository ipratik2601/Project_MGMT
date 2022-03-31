from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.
"""
class CreateProject(CreateView):
    model = Project
    fields = '__all__'
    template_name = 'project/create_project.html'
    success_url = '/project/view/'

class ViewProject(ListView):
    model = Project
    projectlist = model.objects.all()
    context_object_name = 'projectlist'
    template_name = 'project/view_project.html'

class UpdateProject(UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'project/update_project.html'
    success_url = '/project/view/'

class DeleteProject(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = '/project/view/'

class ProjectDetails(DetailView):
    model = Project
    context_object_name = 'projectlist'
    template_name = 'project/project_detail.html'
"""
class about(TemplateView):
    template_name = 'about.html'
#def about (request):
 #   return render(request,'about.html')

def speaker (request):
    return render(request,'speakers.html')

