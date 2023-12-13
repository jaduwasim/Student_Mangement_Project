from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View
from student.forms import StudentRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request, 'student/home.html')

# Student Registraiton Here
def register_user(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
          messages.success(request, 'Congratulation!! Registrarion Success')
          user = form.save()
          return render(request, 'student/studentregistration.html', {'form': form})
    else:
        form = StudentRegistrationForm()
    return render(request, 'student/studentregistration.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are login Now')
                return HttpResponseRedirect('/profile/')
    else:
      form = LoginForm()
      return render(request, 'student/student_login.html',{'form':form})
  
def profile(request):
    return render(request, 'student/profile.html')