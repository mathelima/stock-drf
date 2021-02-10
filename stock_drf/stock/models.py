from django.db import models
from django.db.models import TextField, CharField, IntegerField
# Create your models here.

class Stock(models.Model):
    sku = CharField(max_length=50, blank=False)
    quantity = IntegerField(null=False)
    id_product = IntegerField(null=False)
    id_seller = IntegerField(null=False)
