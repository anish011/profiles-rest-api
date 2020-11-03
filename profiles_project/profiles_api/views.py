from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permisssions

# Create your views here.
class HelloApiView(APIView):
    """Test APU VIew"""

    serializer_class = serializers.HelloSerilaizer

    def get(self, request, format=None):
        temp_list=[
            'First in the list',
            'Second in the list',
            'Third in the list'
        ]
        return Response({'message':'Hello', 'an_apiview':temp_list})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerilaizer

    def list(seld, request):
        a_viewset = [
            'This returns a list with this first line',
            'And this second line',
            'And this third line'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permisssions.UpdateOwnProfile,)
