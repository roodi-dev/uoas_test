from django.db import models

class Printer(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500)
    description = models.TextField()
    features = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

