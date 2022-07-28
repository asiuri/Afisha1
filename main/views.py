from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Category, Director,Movie,Review
from main.serializers import (
    CategorySerializer,
    DirectorSerializer,
    DirectorDetailSerializer,
    MovieSerializer,
    MovieDetailSerializer,
    ReviewSerializer,
    ReviewDetailSerializer
)

@api_view(['GET'])
def categories_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(data=data)


@api_view(['GET','POST'])
def directors_list_view(request):
    if request.method=='GET':
         director=Director.objects.all()
         data=DirectorSerializer(director,many=True).data
         return Response(data=data)
    elif request.method=='POST':
         name=request.data.get('name')
         director= Director.objects.create(

         name=name

         )
         return Response(data=DirectorSerializer(director).data)

@api_view(['GET','PUT','DELETE'])
def director_item_view(request,id):
    try:
       director=Director.objects.get()
    except Director.DoesNotExcist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
       data=DirectorDetailSerializer(director).data
       return Response(data=data)
    elif request.method=='DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        productor = request.data.get('productor')
        director.name=productor
        director.save()
        return Response(data=MovieSerializer(director).data)

@api_view(['GET','POST'])
def movie_list_view(request):
    if request.method=='GET':
         movies=Movie.objects.all()
         data=MovieSerializer(movies,many=True).data
         return Response(data=data)
    elif request.method=='POST':
         name=request.data.get('name')
         text=request.data.get('text')
         time=request.data.get('time')
         director=request.data.get('director')
         category_id=request.data.get('category_id')
         movie=Movie.objects.create(

             title=name,
             description=text,
             duration=time,
             director=director,
             category_id=category_id
         )
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
        name = request.data.get('name')
        text = request.data.get('text')
        time = request.data.get('time')
        director = request.data.get('director')
        category_id = request.data.get('category_id')
        movie.title=name
        movie.description=text
        movie.duration=time
        movie.director=director
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
        opinion = request.data.get('opinion')
        values = request.data.get('values')
        user = request.data.get('user')
        film= request.data.get('film')
        review=Review.objects.create(

            text=opinion,
            stars=values,
            author=user,
            movie=film,

        )
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET','PUT','DELETE'])
def review_item_view(request):
    try:
       review=Review.objects.get()
    except Review.DoesNotExcist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
       data=ReviewDetailSerializer(review).data
       return Response(data=data)
    elif request.method=='DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        opinion = request.data.get('opinion')
        values = request.data.get('values')
        user = request.data.get('user')
        film= request.data.get('film')
        review.text=opinion
        review.stars=values
        review.author=user
        review.movie=film
        review.save()
        return Response(data=MovieSerializer(review).data)




