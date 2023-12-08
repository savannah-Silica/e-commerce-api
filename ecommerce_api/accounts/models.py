from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class CustomUser(AbstractUser):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10, null=True, blank=True)
    
    class Meta:
        verbose_name='user'
        verbose_name_plural='users'
        ordering=['name']
        indexes=[
            models.Index(fields=['email'], name='email_idx',),
            models.Index(fields=['name'], name='name_idx',),
        ]

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo=models.ImageField(default='avatar.jpg', upload_to='profile_pics/%Y')
    date_joined=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='profile'
        verbose_name_plural='profiles'
        ordering=['user']

    def __str__(self):
        return f'Profile of {self.user.name}'
    
    def save(self,**kwargs):
        super().save(**kwargs)
        img=Image.open(self.photo.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
    
    