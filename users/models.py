from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
     
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    ch_r=(
        ("Owner","Owner"),
        ("User","User")
    )
    Role=models.CharField(choices=ch_r,max_length=50)
    contact_number=models.BigIntegerField(default="")

    def __str__(self):
        return self.user.username






