from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    image = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(default='', null=False)
