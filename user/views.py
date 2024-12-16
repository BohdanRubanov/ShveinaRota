from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, "user/profile.html")

def registration(request):
    return render(request, "user/registration.html")

def authorization(request):
    return render(request, "user/authorization.html")