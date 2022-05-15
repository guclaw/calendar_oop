from pprint import pprint as pp

from custom_calendar import Calendar
from event import Event
from helpers.utils import EventGenerator

data = EventGenerator()
data.generate(500)

c = Calendar(data.events)

result = c.get_events_by_date('01-01-2022 00:00')

print(result, len(result))