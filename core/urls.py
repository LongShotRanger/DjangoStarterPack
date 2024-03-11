from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
