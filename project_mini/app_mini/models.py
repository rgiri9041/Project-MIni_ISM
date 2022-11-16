from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

    class Meta:
        db_table = "ims_categories"
    
class AppUser(models.Model):
    fist_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "ims_app_users"

class Item(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    particular = models.TextField(max_length=500)
    ledger_folio = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    entry_date = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "ims_items"