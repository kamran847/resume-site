from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume.urls')),  # مسیر اصلی به اپ resume متصل شد
]
