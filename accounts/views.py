from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UsersSerializer ,CreateUsersSerializer
from rest_framework import status

class AllUsers(APIView):

    def get(self,request):
        users = User.objects.all()
        ser_obj = UsersSerializer(instance=users,many=True)
        return Response(ser_obj.data)
    
    def post (self,request):
        ser_obj = CreateUsersSerializer(data=request.POST)
        if ser_obj.is_valid():
            ser_obj.create(ser_obj.validated_data)
            return Response(ser_obj.data,status=status.HTTP_201_CREATED)
        return Response(ser_obj.errors,status=status.HTTP_400_BAD_REQUEST)
