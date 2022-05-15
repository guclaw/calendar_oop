from pprint import pprint as pp

from custom_calendar import Calendar
from event import Event
from helpers.utils import EventGenerator

data = EventGenerator()
# data.generate(500)


# data.save('./data.json')
events_data = data.load('./data.json')

# pp(events_data)

event = [Event(**event) for event in events_data]

c = Calendar(event)

pp(c)