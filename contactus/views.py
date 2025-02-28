from django.shortcuts import render, redirect
from myproject import settings
from .forms import ContactForm
from .tasks import send_contact_mail_task

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
        send_contact_mail_task.delay(
            subject=f"New Contact Form Submission: {contact.subject}",
            message=f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}",
            from_email= settings.DEFAULT_FROM_EMAIL,
            recipient_mail=[settings.CONTACT_EMAIL]
        )
            
        return redirect("contact")
    else:
        form = ContactForm()
    
    return render(request, "contact_form.html", {"form": form})