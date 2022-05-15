from event import Event


class Workshop(Event):
    def __init__(self, title, location, start_time, duration, owner, participants, kind):
        super().__init__(title, location, start_time, duration, owner, participants)
        self.kind = kind


# w = Workshop('Piwo', 'Orzesze', '19-05-2022 21:25', 35, 'Ala', ['Ola', 'Basia'], 'online')
# print(repr(w))
