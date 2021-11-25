from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Plant
from .serializers import PlantSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/plant-list',
        'Detail': '/plant-detail/<str:pk>/',
        'Create': '/plant-create/',
        'Update': '/plant-update/<str:pk>',
        'Delete': '/plant-delete/<str:pk>',
    }

    return Response(api_urls)


@api_view(['GET'])
def PlantList(request):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PlantDetail(request, pk):
    plants = Plant.objects.get(id=pk)
    serializer = PlantSerializer(plants, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def PlantCreate(request):
    serializer = PlantSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def PlantUpdate(request, pk):
    plant = Plant.objects.get(id=pk)
    serializer = PlantSerializer(instance=plant, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE', 'GET'])
def PlantDelete(request, pk):
    plant = Plant.objects.get(id=pk)
    plant.delete()

    return Response('Delete Complete')
