from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TrekkingGear(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
