from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=150)
    image = models.CharField(max_length=2500)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=255)
    price=models.FloatField( )
    stock=models.IntegerField( )
    image=models.CharField(max_length=2500)

    def __str__(self):
        return self.name

