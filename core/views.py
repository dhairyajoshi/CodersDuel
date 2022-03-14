from tkinter.ttk import PanedWindow
from rest_framework import generics

from group.models import Group
from .models import SubmissionCode
from .serializers import SubmissionSerializer
from rest_framework.decorators import api_view
from .models import NewUser
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from participant.models import Participant

class Submission(generics.ListCreateAPIView):
    queryset= SubmissionCode.objects.all()
    serializer_class= SubmissionSerializer

    def post(self,request,*args,**kwargs):
        regd= request.data['regdno']
        grp= request.data['grp_no']
        code= request.data['code']
        subtime= request.data['subtime']
        participant= Participant.objects.get(regdno=regd)
        grp=Group.objects.get(grp_no=grp)
        submission= SubmissionCode()
        submission.participant=participant
        submission.question=grp.question
        submission.code=code
        submission.subtime=subtime
        submission.grp=grp
        submission.save()
        participant.submission.add(submission)

        return Response({'msg':'code submitted succesfully'})



@api_view(['POST'])
def registerUser(request):  
    usn= request.data.get('username')

    if NewUser.objects.filter(username=usn).exists():
        return Response({'token':'null','code':101})

    serialized= UserSerializer(data=request.data)
    data={}
    if serialized.is_valid():
        instance=serialized.save() 
        refresh = RefreshToken.for_user(instance)
        data['token']=str(refresh.access_token)
        data['code']=200


    return Response(data)

@api_view(['POST'])
def loginUser(request):  
    
    data={}
    reqdata= request.data
    username=reqdata['username']
    password=reqdata['password']

    user = NewUser.objects.get(username=username)
    serialized= UserSerializer(user)

    if user.check_password(password):
        refresh = RefreshToken.for_user(user)
        # data['user']=serialized.data
        data['token']=str(refresh.access_token) 
    
    else: 
        data['error']='wrong credentials'
    

    return Response(data)