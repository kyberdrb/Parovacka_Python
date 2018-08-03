class Couple:

    def __init__(self, pa_gifter, pa_giftee):
        self._gifter = pa_gifter
        self.giftee = pa_giftee
    
    @property
    def first(self):
        return self._gifter
    
    @first.setter
    def first(self, pa_gifter):
        self._gifter = pa_gifter

    @property
    def second(self):
        return self.giftee
    
    @second.setter
    def second(self, pa_giftee):
        self.giftee = pa_giftee
