from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('app_cad/', include('app_cad.urls'))    
] 