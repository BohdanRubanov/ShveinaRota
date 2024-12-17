from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number= models.CharField(max_length=15)
    birth_date=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name="Профіль користувача"
        verbose_name_plural ="Профілі користувачів"