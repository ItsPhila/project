from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    pubdate = models.DateTimeField()
   # myimage = models.ImageField(upload_to='mages/', null=True)
    
    def pre(self):
        return self.text[:8]

    def __str__(self):
        return self.title
