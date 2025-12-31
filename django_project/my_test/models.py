from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    profile = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name or ""
