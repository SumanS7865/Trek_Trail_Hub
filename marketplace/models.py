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
    description = models.TextField()  # लामो वर्णनको लागि
    features = models.TextField(
        help_text="एक-एक लाइनमा फिचर्स लेख्नुहोस्", blank=True
    )  # फिचर्स लिस्टको लागि
    specifications = models.TextField(blank=True)  # तौल, साइज आदि

    # (यसले Database मा फोटो राख्ने बाटो बनाउँछ)
    image = models.ImageField(upload_to="gears/", null=True, blank=True)

    def __str__(self):
        return self.name


class TravelPackage(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=100)
    duration_days = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    # (यसले Package को लागि फोटो राख्ने बाटो बनाउँछ)
    image = models.ImageField(upload_to="packages/", null=True, blank=True)

    def __str__(self):
        return self.title
