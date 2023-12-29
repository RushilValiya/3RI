from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def course(request):
    return render(request, 'course.html')

def register(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/signin")
    else:
        fm = SignupForm()
    return render(request, "register.html", {'form': fm})
def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return render(request, 'feedback.html', {'user': user})

    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'form': fm})
def feedback(request):
    if request.method == 'POST':
        # Process the submitted feedback
        # You can add your logic here

        return render(request, 'feedback.html')

    return render(request, 'feedback.html')
def signout(request):
    logout(request)
    return redirect("/signin")

# Create your views here.
