from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import ProductListAndCreateView, CategoryListAndCreateView, SalesListAndCreateView

schema_view = get_schema_view(
    openapi.Info(
        title='Smartshop API',
        default_version='v1',
        description='This an api that can used to develop smartshop across platforms',
        contact=openapi.Contact(email='nassibshaban345@gmail.com'),
        license=openapi.License(name='MIT License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)


urlpatterns = [
    # urls
    path('products/', ProductListAndCreateView.as_view()),
    path('categories/', CategoryListAndCreateView.as_view(), ),
    path('sales/', SalesListAndCreateView.as_view()),

    # docs
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='Schema-Swagger-UI')
]
