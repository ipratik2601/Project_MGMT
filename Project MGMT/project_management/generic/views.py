from audioop import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class BaseRegisterView(SuccessMessageMixin,FormView):

    form_class = ''#user form goes here from forms.py user
    template_name = ''#registrstion template goes here from template
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save() 
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + "- User Created Successfully...!!!! "

    def get_success_url(self):
        return reverse('')