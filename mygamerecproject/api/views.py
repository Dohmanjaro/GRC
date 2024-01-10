from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelList(APIView):
    def get(self, request):
        data = YourModel.objects.all()
        serializer = YourModelSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
