from django.db import models
import uuid

class Account(models.Model):
    uuid        = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email       = models.EmailField(max_length=254)
    password    = models.CharField(max_length=254)
    card_number = models.IntegerField(blank=True, null=True)
    card_month  = models.IntegerField(blank=True, null=True)
    card_year   = models.IntegerField(blank=True, null=True)
    card_ccv    = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.email

class Snkr(models.Model):
    uuid        = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date        = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    name        = models.CharField(max_length=100, blank=True, null=True)
    price       = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    value       = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    cop         = models.BooleanField(blank=True, null=True)
    
    WANTED_CHOICE = (
        ('t', 'true'),
        ('f', 'false'),
    )
    wanted = models.CharField(
        max_length=1,
        choices=WANTED_CHOICE,
        blank=True,
        default=False,
    )

    def __str__(self):
        return self.name
