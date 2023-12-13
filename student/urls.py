from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from student.views import home, student_login, register_user, profile
urlpatterns = [
    path('', home),
    path('student-registration/', register_user,name='student-reg'),
    path('student-login/', student_login, name='login'),
    path('profile/', profile, name='profile'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)