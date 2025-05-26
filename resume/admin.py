from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'status', 'submitted_at', 'manager_note')  # اضافه کردن یادداشت مدیر برای نمایش
    list_filter = ('status', 'submitted_at')
    search_fields = ('full_name', 'phone_number', 'email')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)
    list_editable = ('status', 'manager_note')  # اجازه ویرایش وضعیت و یادداشت مدیر در صفحه لیست
