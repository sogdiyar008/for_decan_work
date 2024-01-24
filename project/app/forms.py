from .models import *
from django.forms import ModelForm


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['name','info','img','price']
