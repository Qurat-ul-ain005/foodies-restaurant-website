from django.shortcuts import render
from menu.models import Menu
from gallery.models import Gallery
from chef.models import Chef
from testimonial.models import Testimonial

def index(request):

    menu_items = Menu.objects.all()
    gallery_items = Gallery.objects.all()
    chef_items = Chef.objects.all()
    testimonial_items = Testimonial.objects.all()

    return render(request, 'home/index.html', {
        'menu_items': menu_items,
        'gallery_items': gallery_items,
        'chef_items': chef_items,
        'testimonial_items': testimonial_items,
    })