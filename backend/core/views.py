from django.shortcuts import render
from rest_framework import generics, viewsets
from . import models
from . import serializers


class AssetViewSet(viewsets.ModelViewSet):
    queryset = models.Asset.objects.all()
    serializer_class = serializers.AssetSerializer
    def perform_create(self, serializer):
        # Salva l'asset, ma forza il campo 'author' con l'utente attuale (self.request.user)
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
