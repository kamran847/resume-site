from django.db import models

class Resume(models.Model):
    full_name = models.CharField("نام و نام خانوادگی", max_length=100)
    phone_number = models.CharField("شماره تلفن", max_length=20)
    email = models.EmailField("ایمیل", blank=True, null=True)
    resume_file = models.FileField("فایل رزومه", upload_to='resumes/', blank=True, null=True)
    work_experience = models.TextField("سابقه کاری (در صورت نداشتن فایل)", blank=True, null=True)
    address = models.TextField("آدرس")

    submitted_at = models.DateTimeField("تاریخ ارسال", auto_now_add=True)

    def __str__(self):
        return self.full_name
