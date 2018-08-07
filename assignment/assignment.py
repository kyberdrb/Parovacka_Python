from random import shuffle
import copy
from participant import participant

class Assignments:

    def __init__(self, pa_gifter_names):
        self._gifters = self.create_participants(pa_gifter_names)
        self._giftees = copy.copy(self._gifters)

    def create_participants(self, pa_gifter_names):
        participants = []
        for name in pa_gifter_names:
            participants.append(participant.Participant(name))
        return participants

    def create_couples(self):
        while(
                self.deny_giving_gift_to_myself()
                or self.deny_for_reciprocity()
        ):
            shuffle(self._giftees)

    # TODO unittest for True and False scenario
    def deny_giving_gift_to_myself(self):
        for gifter in self._gifters:
            for giftee in self._giftees:
                if self._gifters.index(gifter) == self._giftees.index(gifter):
                    return True
        return False

    # TODO unittest for True and False scenario
    def deny_for_reciprocity(self):
        for gifter in self._gifters:
            for giftee in self._giftees:
                if      self._gifters.index(gifter) == self._giftees.index(giftee) \
                        and \
                        self._gifters.index(giftee) == self._giftees.index(gifter):
                    return True
        return False

    def get_gifters_names(self):
        gifters_names = []
        for gifter in self._gifters:
            gifters_names.append(gifter.name)
        return gifters_names

    def get_giftees_names(self):
        giftees_names = []
        for giftee in self._giftees:
            giftees_names.append(giftee.name)
        return giftees_names

    def list_of_couples(self):
        couples = []
        for i in range(0, len(self._gifters)):
            couples.append("{} <=> {}".format(self._gifters[i].name, self._giftees[i].name))
        return couples
