from django.db import models

class Incident(models.Model):
    participantNo = models.CharField(max_length=255)
    npa_a4_growth = models.CharField(max_length=255)
    dateCollected = models.CharField(max_length=255)
    presence = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    hivExposed = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    serotype = models.CharField(max_length=255)
    vaccine = models.CharField(max_length=255)
    sequence = models.CharField(max_length=255)
