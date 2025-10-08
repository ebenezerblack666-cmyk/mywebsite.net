from django.db import models

class InventoryItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default='fas fa-gavel')
    
    def __str__(self):
        return self.title