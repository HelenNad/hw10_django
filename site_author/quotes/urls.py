from django.urls import path

from . import views
from .templatetags .extract import link_author

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/'+"Albert-Einstein/", views.description_auth, name='root_descript')
]
