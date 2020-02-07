from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    pubdate = models.DateTimeField(default = timezone.now())
    myimage = models.ImageField(upload_to='images/', null=True)
    location = PlainLocationField(based_fields=['city'], zoom=20, null=True)

    def pre(self):
        return self.text[:8]

    def __str__(self):
        return self.title
