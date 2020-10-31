from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test APU VIew"""
    def get(self, request, format=None):
        temp_list=[
            'First in the list',
            'Second in the list',
            'Third in the list'
        ]
        return Response({'message':'Hello', 'an_apiview':temp_list})
