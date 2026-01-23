import os
import sys
import django

# legge til test tickets 
# Slett før PRODUKSJON!

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT_TICKETSYSTEM.settings')
django.setup()
from Ticketapp.models import Tickets
from django.contrib.auth.models import User
from django.db import transaction
import random, datetime


users = list(User.objects.all())


objects = [Tickets(User_id=random.choice(users), Title=f"Test ticket {i}", Description=f"Beskrivelse av Test ticket {i}", Deadline=datetime.date.today() + datetime.timedelta(days=random.randint(1, 30))) for i in range(150)]

chunk_size = 50
with transaction.atomic():
    for i in range(0, len(objects), chunk_size):
        Tickets.objects.bulk_create(objects[i:i + chunk_size])

print(f"Successfully created {len(objects)} tickets!")
