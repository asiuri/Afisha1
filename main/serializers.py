from main.models import Director
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields='id name'.split()

