from django.db import models

class ABTestModel(models.Model):
    variant = models.CharField(max_length=50)
    visitors = models.IntegerField()
    conversions = models.IntegerField()
    conversion_rate = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.variant



class MetricsModel(models.Model):
    variant = models.CharField(max_length=50)
    visitors = models.IntegerField()
    conversions = models.IntegerField()
    conversion_rate = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.variant