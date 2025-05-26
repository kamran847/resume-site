from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # صفحه اصلی اپلیکیشن
    path('form/', views.resume_form, name='resume_form'),  # فرم ارسال رزومه
    path('application_status/<int:id>/', views.application_status, name='application_status'),  # نمایش وضعیت درخواست
]
