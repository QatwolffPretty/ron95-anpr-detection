from django.db import models

class PlateLog(models.Model):
    plate_number = models.CharField(max_length=20)
    country = models.CharField(max_length=50, blank=True, null=True)
    confidence = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plate_number
