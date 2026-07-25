from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact

def save_contact(request):

    if request.method == "POST":

        Contact.objects.create(

            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']

        )

        messages.success(request, "Your message has been sent successfully!")

        return redirect('/')

    return redirect('/')