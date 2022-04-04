from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('accounts/', include('allauth.urls')),

    # rest_framework
    path('api/v1/', include('api.urls')),
    path('api/v1/auth/', include('rest_framework.urls'))

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
