from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('page/<slug:slug>/', views.page, name='page'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('created_by/<int:author_pk>/', views.created_by, name='created_by'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('', views.index, name='index'),
]
