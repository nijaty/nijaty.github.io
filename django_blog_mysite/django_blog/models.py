from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Menu(models.Model):
    home = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.home}"


class News(models.Model):
    title = models.CharField(max_length=200)
    context = models.TextField()
    image = models.ImageField(upload_to="news/")

    publish_date = models.DateField(auto_now_add=True)

    def get_image(self):
        return mark_safe(f"<img style=\'width:90px\' src=\'{self.image.url}\'>")

    def __str__(self):
        return f"{self.title}"
