from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('stocks.urls','stocks'),namespace="stocks")),
    path('api/', include(('stocks.api.urls','api'),namespace="api")), 

]
