from django.shortcuts import render, redirect
from .forms import JobApplicationForm

def apply_for_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'application_success.html') 
    else:
        form = JobApplicationForm()
    return render(request, 'apply.html', {'form': form})