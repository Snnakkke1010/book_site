from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', include('main.urls')),
    path('user/', include('user.urls')),
    path('books/', include('book.urls'))
]
