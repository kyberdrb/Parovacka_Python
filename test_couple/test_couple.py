import unittest
from couple import couple
from participant import participant


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        first_person = participant.Participant(
            pa_name="Lilo",
            pa_has_somebody_to_gift=True
        )
        second_person = participant.Participant(
            pa_name="Stitch",
            pa_has_somebody_to_gift=False
        )
        self.pair = couple.Couple(
            first_person,
            second_person
        )

    def test_first_participant_available(self):
        self.assertIsNotNone(self.pair.first)

    def test_first_participant_name(self):
        self.assertEqual(self.pair.first.name, "Lilo")

    def test_first_participant_availability(self):
        self.assertEqual(self.pair.first.has_somebody_to_gift, True)

    def test_replace_first_participant_name(self):
        person = participant.Participant(
            pa_name="Johny",
            pa_has_somebody_to_gift=True
        )
        self.pair.first = person
        self.assertEqual(self.pair.first.name, "Johny")

    def test_replace_first_participant_availablity(self):
        person = participant.Participant(
            pa_name="Johny",
            pa_has_somebody_to_gift=False
        )
        self.pair.first = person
        self.assertFalse(self.pair.first.has_somebody_to_gift, False)

    def test_second_participant_available(self):
        self.assertIsNotNone(self.pair.second)

    def test_second_participant_name(self):
        self.assertEqual(self.pair.second.name, "Stitch")

    def test_second_participant_availability(self):
        self.assertEqual(self.pair.second.has_somebody_to_gift, False)

    def test_replace_second_participant_name(self):
        person = participant.Participant(
            pa_name="Kenny",
            pa_has_somebody_to_gift=False
        )
        self.pair.second = person
        self.assertEqual(self.pair.second.name, "Kenny")

    def test_replace_second_participant_availablity(self):
        person = participant.Participant(
            pa_name="Kenny",
            pa_has_somebody_to_gift=True
        )
        self.pair.second = person
        self.assertTrue(self.pair.second.has_somebody_to_gift, True)
