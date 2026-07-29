from django.shortcuts import render
from .models import Job

def careers(request):
    jobs = Job.objects.all()
    department = request.GET.get("department")

    if department:
        jobs = jobs.filter(department=department)

    return render(request, "careers/careers.html", {
        "jobs": jobs
    })
