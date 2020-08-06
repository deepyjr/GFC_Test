from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # redirige la page sur la partie blog du projet
    path('',include('blog.urls')),
]
