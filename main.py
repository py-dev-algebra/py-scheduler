from datetime import datetime
from datetime import timedelta

from models.customers import Customer
from models.appointments import Appointment


appointment = Appointment('Demonstracija novog proizvoda',
                          datetime(2024, 3, 15, 15, 00),
                          timedelta(hours=1, minutes=30))

print(appointment)
