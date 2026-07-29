from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            subject=request.POST["subject"],
            message=request.POST["message"]
        )
        return redirect("contact")

    return render(request, "contact/contact.html")