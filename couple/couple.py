class Couple:

    def __init__(self, pa_first, pa_second):
        self._first = pa_first
        self._second = pa_second
    
    @property
    def first(self):
        return self._first
    
    @first.setter
    def first(self, pa_first):
        self._first = pa_first

    @property
    def second(self):
        return self._second
    
    @second.setter
    def second(self, pa_second):
        self._second = pa_second
