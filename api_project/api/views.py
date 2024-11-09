from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Language
from .serializers import LanguageSerializer
# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'list':'/language-list/',
        'Create':'/language-create/',
        'Detail':'/language-detail/<str:pk>/',
        'Update':'/language-update/<str:pk>/',
        'Detete':'/language-delete/<str:pk>/',
    }
    
    return Response(api_urls)


@api_view(['GET'])
def languageList(request):
    languages = Language.objects.all()
    serializer = LanguageSerializer(languages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def languageDetail(request, pk):
    languages = Language.objects.get(id=pk)
    serializer = LanguageSerializer(languages, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def languageCreate(request):
    serializer = LanguageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def languageUpdate(request, pk):
    language = Language.objects.get(id=pk)
    serializer = LanguageSerializer(instance=language,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def languageDelete(request, pk):
    language = Language.objects.get(id=pk)
    language.delete()
    return Response("Language successfully deleted!")