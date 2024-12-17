from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number= forms.CharField(max_length=15, label="Номер телефону")
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)))
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'birth_date', 'password', 'confirm_password']  # Тепер змістили 'confirm_password' після 'password'
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Паролі не збігаються")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Хешуємо пароль

        if commit:
            user.save()

        # Тепер створюємо профіль користувача
        profile = UserProfile.objects.create(
            user=user,
            email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'],
            birth_date=self.cleaned_data['birth_date']
        )
        return user