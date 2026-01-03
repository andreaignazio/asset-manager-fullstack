from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'assets', views.AssetViewSet, basename='asset')
router.register(r'categories', views.CategoryViewSet, basename='category')

urlpatterns=[
    #path("assets/", views.AssetListCreate.as_view(), name="asset-view-create"),
    path("", include(router.urls))
]