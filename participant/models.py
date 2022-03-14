from django.db import models

# Create your models here.

class Participant(models.Model):
    name= models.CharField(max_length=250)
    regdno= models.CharField(max_length=20)
    submission= models.ManyToManyField('core.SubmissionCode',related_name='participant_submission',null=True,blank=True)

    def __str__(self):
        return self.name+' '+self.regdno
