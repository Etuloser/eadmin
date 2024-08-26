from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path("api/v1/eadmin/", include(router.urls)),
    path(
        "api/v1/eadmin/api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
    path("api/v1/eadmin/admin/", admin.site.urls),
    ##################### API 文档配置 #####################
    path("api/v1/eadmin/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/eadmin/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
    #######################################################
]
