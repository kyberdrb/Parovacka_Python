import unittest
from couple import couple
from participant import participant


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.person_1 = participant.Participant(
            pa_name="Lilo",
            pa_has_partner=True
        )
        self.person_2 = participant.Participant(
            pa_name="Stitch",
            pa_has_partner=False
        )
        self.pair = couple.Couple(
            self.person_1,
            self.person_2
        )

    def test_first_participant_available(self):
        self.assertIsNotNone(self.person_1)

    def test_first_participant_name(self):
        self.assertEqual(self.person_1.name, "Lilo")

    def test_first_participant_availability(self):
        self.assertEqual(self.person_1.has_partner, True)

    def test_second_participant_available(self):
        self.assertIsNotNone(self.person_2)

    def test_second_participant_name(self):
        self.assertEqual(self.person_2.name, "Stitch")

    def test_second_participant_availability(self):
        self.assertEqual(self.person_2.has_partner, False)
