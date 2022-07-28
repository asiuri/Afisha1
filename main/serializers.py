from main.models import Category,Director,Movie,Review
from rest_framework import serializers


class CategorySerializer:
    class Meta:
        model=Category
        fields='id name'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields=' name'.split()

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields='name'.split()

class ReviewSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model=Review
        exclude=' id '.split()

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='text stars author movie'.split()



class MovieSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    director=DirectorSerializer()
    reviews=ReviewSerializer(many=True)
    class Meta:
        model=Movie
        fields='id  title description duration director category reviews'.split()

class MovieDetailSerializer(serializers.ModelSerializer):
    filtered_reviews=serializers.SerializerMethodField()
    class Meta:
        model=Movie
        fields='title description filtered_reviews rating'.split()

    def get_filtered_reviews(self,movie):
        review=movie.reviews.filter(stars__gt=3)
        return ReviewSerializer(review,many=True).data






