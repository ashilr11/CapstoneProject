#holds the data that is passed from a csv file.
#In addition, when the server is run these model objects can be used to create a record of data or can be used to access or delete the data.
#The file acts as a way for tables of the model to be created and stored into the sqlite3 database.

from django.db import models

class Incident(models.Model):
    participantID = models.CharField(max_length=255)
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

    def __str__(self):
        return f'{self.participantID}'
