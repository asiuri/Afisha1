from main.models import Category,Director,Movie,Review
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import datetime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='id name'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields='id name'.split()

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields='name'.split()

class DirectorvalidateSerializer:
    author = serializers.CharField(min_length=3, max_length=100)


def validate_author(self, author):
    directors = Director.objects.filter(name=author)
    if directors.count() > 0:
        raise ValidationError('Director name mast be unique!')
    return author

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        exclude=' id movie '.split()

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=' text stars author movie'.split

class ReviewvalidateSerializer(serializers.Serializer):
    opinion=serializers.CharField(required=False)
    values=serializers.IntegerField(max_value=1)
    user=serializers.CharField(min_length=2,max_length=100)
    film=serializers.CharField(min_length=3,max_length=70)




class MovieSerializer(serializers.ModelSerializer):
     category=CategorySerializer()
    # directors=DirectorSerializer()
     reviews=ReviewSerializer(many=True)
     class Meta:
        model=Movie
        fields='id rating title directors description duration  category reviews'.split()

class MovieDetailSerializer(serializers.ModelSerializer):
    filtered_reviews=serializers.SerializerMethodField()
    class Meta:
        model=Movie
        fields='title directors description duration  filtered_reviews rating'.split()

    def get_filtered_reviews(self,movie):
        reviews=movie.reviews.filter(stars__gt=3)
        return ReviewSerializer(reviews,many=True).data

class MovievalidateSerializer(serializers.Serializer):
    name=serializers.CharField(min_length=3,max_length=100)
    text=serializers.CharField(required=False)
    time=serializers.DurationField()
    directors=serializers.CharField(min_length=3,max_length=70)
    category_id=serializers.IntegerField()
    tags=serializers.ListField(child=serializers.IntegerField())

    def validate_category_id(self,category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category doesnot exist!')
        return  category_id

    def validate_name(self,name):
        movie=Movie.objects.filter(title=name)
        if movie.count()>0:
            raise ValidationError('Movie mast be unique!')
        return name