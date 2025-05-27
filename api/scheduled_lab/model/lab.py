from django.db import models

class Lab(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=255)
    count = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'lab'

