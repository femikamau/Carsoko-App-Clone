from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(route="admin/", view=admin.site.urls),
    path(route="apis/", view=include("apis.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
