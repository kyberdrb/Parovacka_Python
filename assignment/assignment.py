from random import shuffle

class Assignments:

    def __init__(self, pa_gifters):
        self.gifters = pa_gifters
        self.giftees = list(pa_gifters)

    def create_list_of_gift_takers(self):
        shuffle(self.giftees)
