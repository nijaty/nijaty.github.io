from django.db import models


class Common(models.Model):
    logo_title = models.CharField(max_length=200)
    logo_url = models.URLField(max_length=200)
    portfolio_title = models.CharField(max_length=200)
    about_title = models.CharField(max_length=200)
    contact_title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.logo_title}"


class Menu(models.Model):
    portfolio = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.portfolio}"


class Head(models.Model):
    img = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    atr = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.logo_img}"


class Portfolio(models.Model):
    atr = models.CharField(max_length=200)
    items = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.atr}"


class About(models.Model):
    atr = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.description}"


class Contact(models.Model):
    about = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.contact}"


class Footer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Icon(models.Model):
    icon = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    section = models.ForeignKey('Footer', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.link}"


class Copyright(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"
