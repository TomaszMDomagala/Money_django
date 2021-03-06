from .models import Category, Spending
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]

class SpendingSerializer(serializers.ModelSerializer):

  class Meta:
    model = Spending
    fields = ('uuid', 'title', 'value', 'description', 'date')