from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name=models.CharField(max_length=255)
    desigination=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self) :
        return self.name


class promoter(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="promoters/")

    def __str__(self) :
        return self.name
