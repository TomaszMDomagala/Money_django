from .models import Times
from rest_framework import serializers


class TimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Times
        fields = ['uuid', 'time', 'date', 'scramble']
