# students/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from student.models import CustomUser, Class
from django.utils.translation import  gettext_lazy as _

class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    phone = forms.CharField(max_length=15, required=True, help_text='Required.')
    date_of_birth = forms.DateField(label="Date of Birth",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    status = forms.BooleanField(initial=False, required=False)
    image = forms.ImageField(required=False)
    student_class = forms.ModelChoiceField(queryset=Class.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'status', 'image', 'student_class')


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
