from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Director
from main.serializers import DirectorSerializer

@api_view(['GET'])
def directors_view(request):
    directors=Director.objects.all()
    data=DirectorSerializer(directors,many=True).data
    return Response(data=data)


@api_view(['GET','POST'])
def movies_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def reviews_view(request):
    return Response(status=status.HTTP_204_NO_CONTENT)


