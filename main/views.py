from django.shortcuts import render, redirect
from .models import Services, Menu, Category, Special_Dishes, Podeia, Gallery, Reservation
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
    return user.groups.filter(name='manager').exists()


def main(request):
    if request.method == 'POST':
        form_reserve = ReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    services = Services.objects.filter(is_visible=True)
    category = Category.objects.filter(is_visible=True)
    menu = Menu.objects.filter(is_visible=True)
    special_dishes = Special_Dishes.objects.filter(is_visible=True)
    podeia = Podeia.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)

    form_reserve = ReservationForm()
    context = {
        'services': services,
        'category': category,
        'menu': menu,
        'forms_reservation': form_reserve,
        'special_dishes': special_dishes,
        'podeia': podeia,
        'gallery': gallery,
    }
    return render(request, 'content.html', context)

def update_reservation(request, pk):
    Reservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('main:list_reservation')



def list_reservations(request):
    message = Reservation.objects.filter(is_processed=False)
    return render(request, 'reservations.html', context={
        'reservation': message
    })
