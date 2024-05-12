from django.contrib import admin
from django.urls import path
from .views import dashboard_view, login_view, logout_view, tables_view, getUser_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard_view),
    path('login/', getUser_view),
    path('logout/', logout_view),
    path('tables/', tables_view)

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
