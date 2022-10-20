from django.urls import path
from .views import *


urlpatterns = [
    path('uploadfile',Upload_file,name='upload'),
    path('show/',upload_show,name='upload_show'),
]
