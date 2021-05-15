from django.db import models
from django.urls import reverse
import uuid

class Category(models.Model):
    name        = models.CharField(max_length=50, help_text='Enter a category of your spending')

    def __str__(self):
        return self.name

class Spending(models.Model):
    uuid        = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID') 
    title       = models.CharField(max_length=100)
    value       = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=1000, blank=True, null=True, help_text='Enter list of items, new line new item')
    category    = models.ManyToManyField(Category, help_text='Select category for this spending')
    date        = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main_page')

    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])

    class Meta:
        ordering = ['date']
