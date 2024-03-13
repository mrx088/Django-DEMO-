from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UsersSerializer ,CreateUsersSerializer,QuestionSerialzer,AnswerSerialzer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from .models import Question,Answer

class AllUsers(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self,request):
        users = User.objects.all()
        ser_obj = UsersSerializer(instance=users,many=True)
        return Response(ser_obj.data)
    



class RegisterUser(APIView):
    def post (self,request):
        ser_obj = CreateUsersSerializer(data=request.POST)
        if ser_obj.is_valid():
            ser_obj.create(ser_obj.validated_data)
            return Response(ser_obj.data,status=status.HTTP_201_CREATED)
        return Response(ser_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    


class AllQuestion(APIView):
    def get(self,request):
        questions = Question.objects.all()
        srz_data = QuestionSerialzer(instance=questions,many=True)
        return Response(srz_data.data,status=status.HTTP_200_OK)


class CreateQuestion(APIView):
    def post(self,request):
        srz_data = QuestionSerialzer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UpdateQuestion(APIView):
    def put(self,request,pk):
        question = Question.objects.get(pk=pk)
        srz_data = QuestionSerialzer(data=request.data,instance=question,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DeleteQuestion(APIView):
    def delete (self,request,pk):
        Question.objects.get(pk=pk).delete()
        return Response({'message':"This Question deleted successfuly"},status=status.HTTP_200_OK)