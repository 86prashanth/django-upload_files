from django.db import models

# Create your models here.
class Upload_files(models.Model):
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='documents/')
    image=models.ImageField(upload_to='images/')