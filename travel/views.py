from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TravelOption, Booking
from .forms import RegisterForm, ProfileForm, BookingForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('travel_list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

def travel_list(request):
    q_type = request.GET.get('type','')
    source = request.GET.get('source','')
    destination = request.GET.get('destination','')
    date = request.GET.get('date','')

    options = TravelOption.objects.all().order_by('date_time')
    if q_type: options = options.filter(type=q_type)
    if source: options = options.filter(source__icontains=source)
    if destination: options = options.filter(destination__icontains=destination)
    if date: options = options.filter(date_time__date=date)

    return render(request, 'travel_list.html', {'options': options, 'filters': {'type': q_type, 'source': source, 'destination': destination, 'date': date}})

@login_required
def book_travel(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['number_of_seats']
            if seats <= 0:
                messages.error(request, 'Number of seats must be positive.')
            elif seats > travel.available_seats:
                messages.error(request, 'Not enough seats available.')
            else:
                total = seats * float(travel.price)
                Booking.objects.create(user=request.user, travel_option=travel, number_of_seats=seats, total_price=total)
                travel.available_seats -= seats
                travel.save()
                messages.success(request, 'Booking confirmed!')
                return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form, 'travel': travel})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status != 'Cancelled':
        booking.status = 'Cancelled'
        booking.save()
        travel = booking.travel_option
        travel.available_seats += booking.number_of_seats
        travel.save()
        messages.info(request, 'Booking cancelled and seats returned.')
    return redirect('my_bookings')
