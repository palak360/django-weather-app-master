from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from . import views


urlpatterns = [
     path('', include('rest_api.urls')),
     path('admin/', admin.site.urls),
     path('show_file/',views.showfile),
]