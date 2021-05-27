from django.urls import path
from . import views

urlpatterns = [
    path('', views.filestorage),
    # path('', views.filestorage),

]
