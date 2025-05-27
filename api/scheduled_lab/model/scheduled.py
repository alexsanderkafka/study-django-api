from django.db import models

class Scheduled(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    user = models.ForeignKey("user", on_delete=models.CASCADE)
    teacher = models.ForeignKey("teacher", on_delete=models.CASCADE)
    lab = models.ForeignKey("lab", on_delete=models.CASCADE)

    #FK com outros models
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'scheduled'
