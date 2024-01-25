from datetime import datetime
from datetime import timedelta
from models.customers import Customer


class Appointment:
    def __init__(self,
                 title: str,
                 start: datetime,
                 duration: timedelta,
                 end: datetime = datetime(1900, 1, 1),
                 attendees: list[Customer] = [],
                 location: str = '',
                 recurrent: int = 0) -> None:
        self.start = start
        self.end = end
        self.duration = duration
        self.title = title
        self.attendees = attendees
        self.location = location
        self.recurrent = recurrent

        self.calculate_end()


    def calculate_end(self):
        self.end = self.start + self.duration


    def __str__(self) -> str:
        appointment_str = f'Naslov: {self.title}\n'
        appointment_str += f'Pocetak: {self.start.strftime("%A, %d.%m.%Y. %H:%M")}\n'
        appointment_str += f'Zavrsetak: {self.end.strftime("%A, %d.%m.%Y. %H:%M")}\n'
        return appointment_str
