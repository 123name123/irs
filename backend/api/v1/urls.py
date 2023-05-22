from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()

router.register('products', views.ProductsViewSet, basename='products')
router.register('favorites', views.FavoritesViewSet, basename='favorites')
router.register('categories', views.CategoriesViewSet, basename='categories')
router.register(r'suppliers', views.SuppliersViewSet,
                basename='suppliers')

urlpatterns = [
    path('', include(router.urls)),
]
