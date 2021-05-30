from django.db import models
import uuid

class Times(models.Model):
    uuid        = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID') 
    time        = models.CharField(max_length=50, null=True, blank=True)
    date        = models.DateTimeField(auto_now=True, blank=True, null=True)
    scramble    = models.CharField(max_length=40, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('rubiks')

    class Meta:
        ordering = ['date']