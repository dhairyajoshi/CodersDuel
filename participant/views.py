from django.shortcuts import render
from rest_framework import generics

from participant.models import Participant
from participant.serializers import ParticipantSerializer

# Create your views here.

class ParticipantCreate(generics.ListCreateAPIView):

    queryset= Participant.objects.all()
    serializer_class= ParticipantSerializer
