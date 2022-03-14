from urllib import request
from xml.etree.ElementTree import QName
from rest_framework import generics
from .models import Question
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import QuestionSerializer
# Create your views here.

class QuestionSet(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = QuestionSerializer
    def get(self,request,*args,**kwargs):

        if request.user.is_staff:
            queryset= Question.objects.all()
            serialized= QuestionSerializer(queryset,many=True)
            return Response(serialized.data)

        return Response({'msg':'You don\'t have the permission to view this page'})

    def post(self,request,*args,**kwargs):
        if request.user.is_staff:

            serialized= QuestionSerializer(data=request.data)

            if serialized.is_valid():
                qst=serialized.save()
                qst.user=request.user
                qst.username=request.user.username
                qst.save()

                return Response({'msg':'question added successfully'})

            else:
                return Response(serialized.errors)

        return Response({'msg':'Not authorized'})



