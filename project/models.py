from django.db import models

class Widget(models.Model):
    name = models.CharField(max_length=100)
    api_endpoint = models.URLField()
    config = models.JSONField()

    def __str__(self):
        return self.name
