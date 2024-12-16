from django.db import models
from django.contrib.auth.models import User

class MasterClass (models.Model):
    title = models.CharField(max_length=50, verbose_name="Назва")
    instructionImg1 = models.ImageField(upload_to = 'masterclass_images/', verbose_name="Фото-інструкція1", null=True, blank=True )
    instructionImg2 = models.ImageField(upload_to = 'masterclass_images/', verbose_name="Фото-інструкція2", null=True, blank=True )
    video = models.URLField(verbose_name="Посилання на відео", null=True, blank=True)
    examplesImg1 = models.ImageField(upload_to = 'masterclass_images/', verbose_name="Фото-приклад1", null=True, blank=True )
    examplesImg2 = models.ImageField(upload_to = 'masterclass_images/', verbose_name="Фото-приклад2", null=True, blank=True )
    examplesImg3 = models.ImageField(upload_to = 'masterclass_images/', verbose_name="Фото-приклад3", null=True, blank=True )
    injuredImg1 = models.ImageField(upload_to = 'masterclass_images/', verbose_name="Фото на пораненому 1", null=True, blank=True )
    injuredImg2 = models.ImageField(upload_to = 'masterclass_images/', verbose_name="Фото на пораненому 2", null=True, blank=True )
    injuredImg3 = models.ImageField(upload_to = 'masterclass_images/', verbose_name="Фото на пораненому 3", null=True, blank=True )
    information= models.TextField(verbose_name="Інформація")
    author = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="Автор", null=True, blank=True)
    date = models.DateTimeField(verbose_name="Час публікації")  

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Майстер-клас"
        verbose_name_plural ="Майстер-класи"
class Comments (models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="Автор", null=True, blank=True)
    comment= models.TextField(verbose_name="Коментарій")
    date = models.DateTimeField(verbose_name="Час публікації")
