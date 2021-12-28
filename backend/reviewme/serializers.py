from rest_framework import serializers
from reviewme.models import *
from rest_framework import routers, viewsets


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class RestrauntSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name'
    )

    class Meta:
        model = Restraunt
        fields = ['name', 'city', 'state', 'category_name']


class ReviewsSerializer(serializers.ModelSerializer):
    restraunt_name = serializers.CharField(
        source='restraunt.name', read_only=True)

    class Meta:
        model = Reviews
        fields = ['restraunt_name', 'timestamp', 'rating', 'comment']
