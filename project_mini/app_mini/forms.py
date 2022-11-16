from django import forms
from .models import Item

class ItemCreateForm(forms.ModelForm):
    class Meta:
        # If you need all fields then use fields = "__all__" else use following one
        fields = ("title", "category", "particular", \
            "ledger_folio", "quantity", "price")
        model = Item


