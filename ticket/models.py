from django.db import models
from django.conf import settings

class Ticket(models.Model):
    title = models.CharField(max_length=25, unique=True)
    content = models.TextField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=25)
    category = models.CharField(max_length=100, choices = settings.CATEGORY_CHOICES)
    created_on = models.DateField(auto_now_add=True)

    class Meta: 
        db_table = 'TICKET'
        ordering = ['-created_on']

    def __str__(self):
        return self.title