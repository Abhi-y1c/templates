from django.urls import path
from.views import *


urlpatterns = [
        path("app1/",home1,name="home"),
]