from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    charge_full = models.BooleanField(default=False, verbose_name='Оплатил')
