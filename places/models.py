from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

class Places(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50)
    pubdate = models.DateTimeField(default = timezone.now())
    myimage = models.ImageField(upload_to='images/', null=True)


    def pre(self):
        return self.text[:8]

    def __str__(self):
        return self.title
