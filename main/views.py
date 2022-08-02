from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from main.models import Category, Director,Movie,Review
from main.serializers import (
    CategorySerializer,
    DirectorSerializer,
    DirectorDetailSerializer,
    DirectorvalidateSerializer,
    MovieSerializer,
    MovieDetailSerializer,
    MovievalidateSerializer,
    ReviewSerializer,
    ReviewDetailSerializer,
    ReviewvalidateSerializer,


)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def categories_view(request):
    print(request.user)
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(data=data)


@api_view(['GET','POST'])
def directors_list_view(request):
    if request.method=='GET':
         directors=Director.objects.all()
         data=DirectorSerializer(directors,many=True).data
         return Response(data=data)
    elif request.method=='POST':
        serializer = DirectorvalidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        author=serializer.validated_data.get('author')
        directors= Director.objects.create(

           name=author

        )
        return Response(data=DirectorSerializer(directors).data)



@api_view(['GET','PUT','DELETE'])
def directors_item_view(request,id):
    try:
       directors=Director.objects.get(id=id)
    except Director.DoesNotExcist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
       data=DirectorDetailSerializer(directors).data
       return Response(data=data)
    elif request.method=='DELETE':
        directors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = DirectorvalidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        author= request.data.get('author')
        directors.name=author
        directors.save()
        return Response(data=DirectorSerializer(directors).data)

@api_view(['GET','POST'])
def movie_list_view(request):
    if request.method=='GET':
         movies=Movie.objects.all()
         data=MovieSerializer(movies,many=True).data
         return Response(data=data)
    elif request.method=='POST':
         serializer=MovievalidateSerializer(data=request.data)
         if  not serializer.is_valid():
             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                             data={'errors':serializer.errors})
         name=serializer.validated_data.get('name')
         text=serializer.validated_data.get('text')
         time=serializer.validated_data.get('time')
         directors=serializer.validated_data.get('directors')
         category_id=serializer.validated_data.get('category_id')
         movie=Movie.objects.create(

             title=name,
             description=text,
             duration=time,
             directors=directors,
             category_id=category_id
         )
         movie.tags.set(serializer.validated_data['tags'])
         return Response(data=MovieSerializer(movie).data)

@api_view(['GET','PUT','DELETE'])
def movie_item_view(request,id):
    try:
       movie=Movie.objects.get(id=id)
    except Movie.DoesNotExcist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
       data=MovieDetailSerializer(movie).data
       return Response(data=data)
    elif request.method=='DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovievalidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = request.data.get('name')
        text = request.data.get('text')
        time = request.data.get('time')
        directors = request.data.get('directors')
        category_id = request.data.get('category_id')
        movie.title=name
        movie.description=text
        movie.duration=time
        movie.directors=directors
        movie.category_id=category_id
        movie.save()
        return Response(data=MovieSerializer(movie).data)

@api_view(['GET','POST'])
def reviews_view(request):
    if request.method=='GET':
        reviews=Review.objects.all()
        data=ReviewSerializer(reviews,many=True).data
        return Response(data=data)
    elif request.method=='POST':
        serializer = ReviewvalidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})

        opinion =serializer.validated_data.get('opinion')
        values = serializer.validated_data.get('values')
        user = serializer.validated_data.get('user')
        film= serializer.validated_data.get('film')
        review=Review.objects.create(

            text=opinion,
            stars=values,
            author=user,
            movie=film,

        )
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET','PUT','DELETE'])
def reviews_item_view(request,id):
    try:
       review=Review.objects.get(id=id)
    except Review.DoesNotExcist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
       data=ReviewDetailSerializer(review).data
       return Response(data=data)
    elif request.method=='DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ReviewvalidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        opinion = request.data.get('opinion')
        values = request.data.get('values')
        user = request.data.get('user')
        film= request.data.get('film')
        review.text=opinion
        review.stars=values
        review.author=user
        review.movie=film
        review.save()
        return Response(data=ReviewSerializer(review).data)




