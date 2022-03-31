from django.shortcuts import render
from django.urls import reverse_lazy
from generic.views import*
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
class RegisterUserView(BaseRegisterView):
    template_name = 'user/registration.html'

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        if user.role == 'Admin':
            user.is_superuser = True
        else:
            user.is_superuser = False
        user.is_active = True
        user.is_staff = True
        user.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('user_urls:login')

class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('user_urls:/')#redirect url goes here