"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bands/", views.band_list, name="band-list"),
    path("bands/<int:band_id>/", views.band_detail, name="band-detail"),
    path("bands/add/", views.band_create, name="band-create"),
    path("bands/<int:band_id>/udpate", views.band_update, name="band-update"),
    path("about-us/", views.about, name="about-us"),
    path("contact-us/", views.contact, name="contact-us"),
    path("ads/", views.ads, name="ads-list"),
    path("ads/<int:ad_id>/", views.ad_detail, name="ad-detail"),
    path("ads/add", views.ad_create, name="ad-create"),
    path("ads/<int:ad_id>/update/", views.ad_update, name="ad-update"),
    path("confirmation/", views.confirmation, name="email-sent"),
    path("", views.band_list, name="home")
]
