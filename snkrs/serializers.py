from .models import Account, Snkr
from rest_framework import serializers


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['uuid', 'email', 'password', 'card_number', 'card_month', 'card_year', 'card_ccv']


class SnkrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snkr
        fields = ['uuid', 'name', 'value', 'price', 'date']