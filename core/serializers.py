from rest_framework import serializers
from .models import SubmissionCode
from rest_framework import serializers
from .models import NewUser


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = NewUser
        fields = ('username', 'first_name', 'password','is_staff')
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 

class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model= SubmissionCode
        fields='__all__' 