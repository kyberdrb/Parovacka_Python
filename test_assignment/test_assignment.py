import unittest
from couple import couple
from participant import participant
from assignment import assignment


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.first_person = participant.Participant(
            pa_name="Lilo",
        )
        self.second_person = participant.Participant(
            pa_name="Stitch",
        )
        self.third_person = participant.Participant(
            pa_name="Monk",
        )
        self.pair = couple.Couple(
            self.first_person,
            self.second_person
        )
        self.participants_list = [
            self.first_person,
            self.second_person,
            self.third_person
        ]
        self.assignments = assignment.Assignments(self.participants_list)

    def test_first_participant_assignment(self):
        self.assertEqual(self.assignments.gifters[0].name, "Lilo")

    def test_third_participant_assignment(self):
        self.assertEqual(self.assignments.gifters[2].name, "Monk")

    def test_nonexistent_participant_assignment(self):
        # self.assertRaises(IndexError, self.assignments.gifters[3].name)
        pass

    def test_first_giftee(self):
        self.assertEqual(self.assignments.giftees[0].name, "Lilo")

    def test_third_giftee(self):
        self.assertEqual(self.assignments.giftees[2].name, "Monk")

    def test_nonexistent_giftee(self):
        # self.assertRaises(IndexError, self.assignments.giftees[3].name)
        pass
