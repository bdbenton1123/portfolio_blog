from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("projects.urls")),
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("musica_primus/", include("musica_primus.urls")),
]
