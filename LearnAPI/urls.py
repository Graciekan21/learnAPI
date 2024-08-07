"""learnapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from LearnAPI import views
from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route
from django.urls import path
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", root_route),
    path("admin/", admin.site.urls),
    # path('api/', include('LearnAPI.urls')),
    path("api-auth/", include("rest_framework.urls")),
    # our logout route has to be above the default one to be matched first
    path("dj-rest-auth/logout/", logout_route),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    # file, add endpoints for obtaining and refreshing tokens.
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include("profiles.urls")),
    path("", include("posts.urls")),
    path("", include("comments.urls")),
    path("", include("likes.urls")),
    path("", include("followers.urls")),
    path("", include("notifications.urls")),
    path("", include("reports.urls")),
]
