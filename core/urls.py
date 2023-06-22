from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(route="admin/", view=admin.site.urls),
    path(route="apis/", view=include("apis.urls")),
]
