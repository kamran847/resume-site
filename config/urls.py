from django.contrib import admin
from django.urls import path, include  # برای include کردن مسیرهای اپ resume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume.urls')),  # مسیر اصلی به اپ resume متصل شد
]

