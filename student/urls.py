from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index,),
    path('login', Login, name='login'),
    path('home/', HomeView, name='home'),
    path('info/', InfoView, name='info'),
    path("studentedit/<int:pk>/", StudentEdit, name='edit'),
    path("infoedit/<int:pk>/", InfoEdit, name='infoedit'),
    path("infodelete/<int:pk>/", InfoDelete, name='infodelete'),
    path("studentdelete/<int:pk>/", StudentDelete, name='delete'),
    path("create/", StudentCreate, name='create'),
    path("info-create/", InfoCreate, name='infocreate'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
