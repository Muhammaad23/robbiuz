from rest_framework import serializers
from django.utils.translation import gettext as _
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'created_at']

    def to_representation(self, instance):
        """Tarjima qilingan maydonlarni qaytarish uchun"""
        representation = super().to_representation(instance)
        representation['name'] = _(instance.name)  # Name tarjima qilinadi
        representation['description'] = _(instance.description)  # Description tarjima qilinadi
        return representation
