from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # مسیر صفحه اصلی
    path('form/', views.resume_form, name='resume_form'),  # مسیر فرم استخدام
]
