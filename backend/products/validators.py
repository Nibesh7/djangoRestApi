from rest_framework import serializers

from .models import Product

def validate_title(value): #validate_field_name
    qs = Product.objects.filter(title__iexact=value)
    #iexact is for case insensitive
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name")
    return value