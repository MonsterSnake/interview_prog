from django.db import models

# Create your models here.


class category(models.Model):
    name = models.TextField(null=True, blank=True)

class products(models.Model):
    category_id = models.IntegerField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    status = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
