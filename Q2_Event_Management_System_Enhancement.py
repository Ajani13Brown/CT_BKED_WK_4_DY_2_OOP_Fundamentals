class Event:
        def __init__(self, name, date, participants,):
            self.name = name
            self.date = date
            self.participants = participants

        def add_participant(self):
              new_participants = int(input('How many participants would you like to add to the event: ' ))
              self.participants += new_participants
              print(f'There have been {new_participants} added to {self.name} for a total of {self.participants} participants')

        def get_participant_count(self):
              print(f'{self.name} currently has a total of {self.participants} participants.')

woodstock = Event("Woodstock", 1969, 460000)

woodstock.get_participant_count()