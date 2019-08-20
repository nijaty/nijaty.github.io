from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    expire_date = models.DateTimeField()
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-id"]