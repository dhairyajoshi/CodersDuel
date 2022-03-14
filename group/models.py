from django.db import models
from participant.models import Participant
# Create your models here.
class Group(models.Model):
    grp_no= models.IntegerField()
    participants= models.ManyToManyField(Participant,related_name='group_participant')
    question= models.ForeignKey('question.Question',on_delete=models.PROTECT,null=True)

    def __str__(self) :
        return str(self.grp_no)