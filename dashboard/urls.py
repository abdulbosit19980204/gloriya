from django.contrib import admin
from django.urls import path
from .views import dashboard_view, login_view, logout_view

urlpatterns = [
    path('/', dashboard_view),
    path('login/', login_view),
    path('logout/', logout_view)
]
