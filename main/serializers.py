from main.models import Director,Movie,Review
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields='id name'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        exclude='id  '.split()


class MovieSerializer(serializers.ModelSerializer):
    directors=DirectorSerializer()
    reviews=ReviewSerializer(many=True)
    class Meta:
        model=Movie
        fields='id rating title description duration directors reviews'.split()

class MovieDetailSerializer(serializers.ModelSerializer):
    filtered_reviews=serializers.SerializerMethodField()
    class Meta:
        model=Movie
        fields='title description filtered_reviews rating'.split()

    def get_filtered_reviews(self,movie):
       # review=Review.objects.filter(movie=movie,stars__gt=3)
        review=movie.reviews.filter(stars__gt=3)
        return ReviewSerializer(review,many=True).data