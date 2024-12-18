from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Логін", max_length=150)
    email = forms.EmailField(label="Електронна пошта")
    phone_number = forms.CharField(max_length=15, label="Номер телефону")
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), label="Дата народження")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Підтвердження паролю")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'birth_date', 'password', 'confirm_password']

    def clean_confirm_password(self):
        # Отримуємо паролі
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        # Перевіряємо, чи вони збігаються
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Паролі не збігаються!")  # Помилка для конкретного поля

        return confirm_password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ця електронна пошта вже використовується!")
        return email

    def save(self, commit=True):
        # Прежде чем сохранить, проверяем, что форма валидна
        if not self.is_valid():
            raise forms.ValidationError("Форма невалидна. Проверьте данные.")

        # Создаем пользователя, если форма валидна
        user = super().save(commit=False)
        
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("Ця електронна пошта вже використовується!")
        
        user.set_password(self.cleaned_data['password'])  # Хешируем пароль

        if commit:
            user.save()

        # Создаем профиль пользователя
        profile = UserProfile.objects.create(
            user=user,
            email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'],
            birth_date=self.cleaned_data['birth_date']
        )

        return user