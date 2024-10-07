from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("question/", include("question.urls")),
    path("answer/", include("answer.urls")),
]
