from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question,Answer


class UsersSerializer(serializers.ModelSerializer):

    class Meta : 
        model = User
        fields = ['username','email','password',]
        extra_kwargs = {'password': {'write_only': True}}






def CheckUsername(value):
    if len(value) <= 4 :
        raise serializers.ValidationError('Username musst upper than 4 Char')

class CreateUsersSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta : 
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'username':{'validators':[CheckUsername]},
            'password': {'write_only': True},
            }
    


    def create(self, validated_data):
        del validated_data['password2']
        user = User.objects.create_user(username=validated_data['username'],email=validated_data['email'],password=validated_data['password'],)
        return user

    def validate(self, data):
        if data['password']!= data['password2']:
            raise serializers.ValidationError("Passwords dont mach together")
        return data

    def validate_email(self,value):
        if "admin" in value.lower():
            raise serializers.ValidationError('You cant create this Email')
        return value
    

class QuestionSerialzer(serializers.ModelSerializer):

    answer = serializers.SerializerMethodField()
    class Meta :
        model = Question
        fields = '__all__'

    def get_answer(self,obj):
        answers_obj = obj.answers.all()
        return AnswerSerialzer(instance=answers_obj,many=True).data


class AnswerSerialzer(serializers.ModelSerializer):
    class Meta :
        model = Answer
        fields = '__all__'