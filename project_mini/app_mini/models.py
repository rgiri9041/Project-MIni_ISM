from django.db import models
from datetime import datetime
# Create your models here.
class Category(models.Model):
    #Charfield vanako text vako huna lay lekhako ho . tesma int, email etc hunxa as requirement.
    Category = models.CharField(max_length = 200)

    class Meta:
        db_table = "ims_categories" # creating table name. it is not compulsary if we won't write then django will make it self.

class AppUser(models.Model):
    first_name = models.CharField(max_length = 100 )
    middle_name = models.CharField(max_length = 100, null = True, blank = True)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)

    class Meta:
        db_table = "ims_app_users"

class Items(models.Model):
    title = models.CharField(max_length=200)
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)
    particular = models.TextField(max_length = 500)
    ledger_folio = models.CharField(max_length = 100, null = True, blank = True)
    quantity = models.IntegerField()
    prince = models.FloatField()
    total = models.FloatField()
    entry_date = models.DateTimeField(default = datetime.now())

    class Meta:
        db_table = "ims_items"
