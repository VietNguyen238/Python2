from django.db import models

# Create your models here.
class NhatKy(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media', null=True)
    audio = models.FileField(upload_to="media/music", null=True)
    def __str__(self):  
        return self.title