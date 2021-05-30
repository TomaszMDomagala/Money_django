from django.shortcuts import render
from rubik.models import Times
from .serializers import TimeSerializer
from rest_framework import viewsets
from django.views.generic import (
        ListView,
        DetailView,
        DeleteView
        )

class RubikViews(ListView):
    model = Times

class TimesViewSet(viewsets.ModelViewSet):
    serializer_class    = TimeSerializer
    queryset            = Times.objects.all()
