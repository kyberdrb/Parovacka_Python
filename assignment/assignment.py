from random import shuffle
from participant import participant
from couple import couple

class Assignments:

    def __init__(self, pa_gifters):
        # TODO rework from two lists to one list of Couple objects
        self.gifters = pa_gifters
        self.giftees = list(pa_gifters)

    def create_list_of_giftees(self):
        shuffle(self.giftees)
