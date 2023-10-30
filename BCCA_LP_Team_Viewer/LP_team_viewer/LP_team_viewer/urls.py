"""
URL configuration for LP_team_viewer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import (
    landing_page,
    documentation_page,
    community_page,
    procurement_page,
    management_page,
)

urlpatterns = [
    path("", landing_page),
    path("management", management_page),
    path("procurement", procurement_page),
    path("community", community_page),
    path("documentation", documentation_page),
    path("admin/", admin.site.urls),
]
