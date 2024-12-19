from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def logout_view(request):
    logout(request)  # Вихід користувача
    return redirect('profile') 

def profile(request):
    if request.user.is_authenticated:
        return render(request, "user/profile.html", {'user': request.user})
    else:
       return render(request, "user/profile.html")
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Зберігаємо користувача та профіль
            login(request, user)  # Логін користувача після реєстрації
            return redirect('profile')  # Перенаправляємо на домашню сторінку
    else:
        form = UserRegistrationForm()  # Якщо GET запит, виводимо порожню форму
    return render(request, "user/registration.html", {'form': form})

def authorization(request):
    if request.method == "POST":
        # Отримуємо дані з форми
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Перевіряємо, чи існує користувач
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Якщо користувач знайдений, авторизуємо
            login(request, user)
            messages.success(request, "Вітаємо, ви успішно увійшли!")
            return redirect('profile')  # Перенаправлення після успішного входу
        else:
            # Якщо користувач не знайдений
            messages.error(request, "Невірне ім'я користувача або пароль.")
            return redirect('authorization')  # Повторний перехід на сторінку логіну
        
    return render(request, "user/authorization.html")