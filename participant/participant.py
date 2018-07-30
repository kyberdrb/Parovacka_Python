class Participant:

    def __init__(self, pa_name, pa_has_partner):
        self._name = pa_name
        self._has_partner = pa_has_partner

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, pa_name):
        self._name = pa_name

    @property
    def has_partner(self):
        return self._has_partner

    @has_partner.setter
    def has_partner(self, pa_has_partner):
        self._has_partner = pa_has_partner
