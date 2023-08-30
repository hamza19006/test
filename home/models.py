from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=50)
    des = models.TextField()