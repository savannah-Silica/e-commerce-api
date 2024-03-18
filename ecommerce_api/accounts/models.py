from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin
from PIL import Image
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(_("email address"), unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_joined=models.DateTimeField(default=timezone.now)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    def __str__(self):
        return self.email
class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo=models.ImageField(default='avatar.jpg', upload_to='profile_pics/%Y')
    date_joined=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='profile'
        verbose_name_plural='profiles'
        ordering=['user']

    def __str__(self):
        return f'Profile of {self.user.email}'
    
    def save(self,**kwargs):
        super().save(**kwargs)
        img=Image.open(self.photo.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
    
    