from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
]
