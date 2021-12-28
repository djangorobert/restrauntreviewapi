from rest_framework import viewsets
from reviewme.models import *
from .serializers import CategorySerializer, RestrauntSerializer, ReviewsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RestrauntViewSet(viewsets.ModelViewSet):
    queryset = Restraunt.objects.all()
    serializer_class = RestrauntSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
