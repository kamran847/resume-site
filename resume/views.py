from django.shortcuts import render, redirect
from .forms import ResumeForm

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'resume/success.html')  # نمایش صفحه موفقیت
    else:
        form = ResumeForm()
    return render(request, 'resume/resume_form.html', {'form': form})
def home(request):
    return render(request, 'resume/home.html')  # باید فایل home.html رو هم داشته باشی
