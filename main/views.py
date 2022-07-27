from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Director,Movie
from main.serializers import DirectorSerializer,MovieSerializer,MovieDetailSerializer

@api_view(['GET'])
def directors_view(request):
    directors=Director.objects.all()
    data=DirectorSerializer(directors,many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_list_view(request):
    movies=Movie.objects.all()
    data=MovieSerializer(movies,many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_item_view(request,id):
    try:
       movie=Movie.objects.get(id=id)
    except Movie.DoesNotExcist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data=MovieDetailSerializer(movie).data
    return Response(data=data)

@api_view(['GET'])
def reviews_view(request):
    return Response(status=status.HTTP_204_NO_CONTENT)


