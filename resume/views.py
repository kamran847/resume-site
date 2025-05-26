from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm
from .models import Resume  # مدل رزومه

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            # هدایت کاربر به صفحه نمایش وضعیت درخواست با شناسه رزومه ذخیره شده
            return redirect('application_status', id=application.id)
    else:
        form = ResumeForm()
    return render(request, 'resume/resume_form.html', {'form': form})

def home(request):
    return render(request, 'resume/home.html')

def application_status(request, id):
    application = get_object_or_404(Resume, id=id)
    context = {
        'application': application
    }
    return render(request, 'application_status.html', context)
