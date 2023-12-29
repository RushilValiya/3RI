from django.contrib import admin
from django.urls import path
from .views import home, about, contact, course, register, signin, signout, feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('course/', course, name="course"),
    path('signup/', register, name="signup"),
    path('signin/', signin, name="signin"),
    path('signout/', signout, name="signout"),
    path('feedback/', feedback, name='feedback'),
]