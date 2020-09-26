"""Boxoffice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as user_views
from theater import views as theater_views
from movie import views as movie_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',user_views.LoginView.as_view(),name='login'),
    path('logout/',user_views.LogoutView.as_view(),name='logout'),
    path('register/',user_views.CreateUserView.as_view(),name='register'),

    path('theater/api/',theater_views.ManageTheaterAPIView.as_view(),name='theater-api'),
    path('theater/api/<int:id>/',theater_views.ManageTheaterDetailAPIView.as_view(),name='theater-detail-api'),
    path('theater/api/<int:id>/shows/',theater_views.ManageShowAPIView.as_view(),name='theater-show-api'),

    path('movie/api/',movie_views.ManageMovieAPIView.as_view(),name='movie-api'),
    path('movie/api/<int:id>/',movie_views.ManageMovieDetailAPIView.as_view(),name='movie-detail-api'),
    path('movie/search/api/',movie_views.SearchMovieAPIView.as_view(),name='movie-search-api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
