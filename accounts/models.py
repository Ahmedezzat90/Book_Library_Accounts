
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
import datetime
from django.utils.text import slugify

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    image  = models.ImageField(upload_to='profile/')
    join_date = models.DateTimeField(("join date"),default = datetime.datetime.now)




    def __str__(self):
        return str(self.user)

## create new user ---> create new empty profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



