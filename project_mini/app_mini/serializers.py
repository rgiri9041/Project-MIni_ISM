from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("title", "category", "particular", "legder_folio", "quantity", "price", "entry_date")
        model = Item