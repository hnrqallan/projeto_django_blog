from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('page/', views.page, name='page'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('', views.index, name='index'),
]
