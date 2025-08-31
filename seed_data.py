import os
import django
import datetime
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_booking.settings')
django.setup()

from travel.models import TravelOption

# Clear old data
TravelOption.objects.all().delete()

# Create sample travel options
TravelOption.objects.create(
    type="Flight",
    source="Delhi",
    destination="Mumbai",
    date_time=timezone.now() + datetime.timedelta(days=1),
    price=5000.00,
    available_seats=50
)

TravelOption.objects.create(
    type="Train",
    source="Delhi",
    destination="Jaipur",
    date_time=timezone.now() + datetime.timedelta(days=2),
    price=1200.00,
    available_seats=150
)

TravelOption.objects.create(
    type="Bus",
    source="Bangalore",
    destination="Chennai",
    date_time=timezone.now() + datetime.timedelta(days=1, hours=5),
    price=800.00,
    available_seats=40
)

print("✅ Sample travel options added successfully!")
