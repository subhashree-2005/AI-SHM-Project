from django.db import models

class SensorData(models.Model):

    frequency = models.FloatField()

    rms = models.FloatField()

    status = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.status