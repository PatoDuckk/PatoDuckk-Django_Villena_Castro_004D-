from django.urls import path 
from django.contrib import admin
from django.conf.urls import include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jardineria.urls')),
    path('compra', views.compra),
    path('Contactanos', views.Contactanos),
    path('index', views.index),
    path('indexgaleria', views.indexgaleria),
    path('quienessomos', views.quienessomos),
    path('register', views.register),
    
]