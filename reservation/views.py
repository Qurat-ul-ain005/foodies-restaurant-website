from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation


def save_reservation(request):

    if request.method == "POST":

        Reservation.objects.create(

            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            guests=request.POST['guests'],
            date=request.POST['date'],
            time=request.POST['time'],
            message=request.POST['message']

        )
        messages.success(request, "Your table has been booked successfully!")
        return redirect('/')

    return redirect('/')