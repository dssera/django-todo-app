from django.db import models

# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=6, choices={'UDN': 'Undone', 
                                                     'DN': 'Done'})
    created_at = models.DateTimeField(auto_now_add=True)

