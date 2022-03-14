from tkinter.tix import Balloon
from django.db import models

# Create your models here.
class Question(models.Model):

    problem= models.TextField()
    user= models.ForeignKey('core.NewUser',on_delete=models.PROTECT,null=True)
    username= models.CharField(max_length=250,null=True)
    groups= models.ManyToManyField('group.Group',related_name='question_groups',null=True,blank=True)

    def __str__(self) :
        return self.problem