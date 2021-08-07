from django.db import models

class Mens(models.Model):
    name = models.CharField(max_length=20)
    slug =  models.CharField(max_length=20 , null=False , unique=True)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/mens/')

    @staticmethod
    def get_all_product():
        return Mens.objects.all()