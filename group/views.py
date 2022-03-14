from rest_framework.response import Response
from rest_framework import generics
from .models import Group
from participant.models import Participant
from question.models import Question
import random
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from .serializers import GroupSerializer

# Create your views here.
class CreateGroup(generics.ListCreateAPIView):

    queryset= Group.objects.all()
    serializer_class= GroupSerializer

    def post(self,request,*args,**kwargs):
        
        grp_no= request.data['grp_no']
        regd= request.data['regdno']
        participant= Participant.objects.get(regdno=regd)
        grp = Group.objects.filter(grp_no=grp_no)

        if not grp:
            grp= Group()
            grp.grp_no=grp_no
            qst= random.choice(Question.objects.all())
            grp.question=qst
            grp.save()
            grp.participants.add(participant)
            qst.groups.add(grp)
            qst.save()

            return Response({'question':qst.problem},status=HTTP_200_OK)

        elif len(grp)==1:
            grp=grp.first()
            if grp.participants.all().count()==2:
                return Response({'msg':'Group full'},status=HTTP_400_BAD_REQUEST)
            grp.participants.add(participant)
            grp.save()

            return Response({'question':grp.question.problem},status=HTTP_200_OK)

            
            
