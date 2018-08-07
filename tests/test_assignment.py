import unittest
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
        self.participants = [
            self.first_person,
            self.second_person,
            self.third_person
        ]
        self.participant_names = []
        for someone in self.participants: self.participant_names.append(someone.name)

        self.assignments = assignment.Assignments(self.participant_names)

    def test_first_participant_assignment(self):
        self.assertEqual(self.assignments._gifters[0].name, "Lilo")

    def test_third_participant_assignment(self):
        self.assertEqual(self.assignments._gifters[2].name, "Monk")

    def test_first_giftee(self):
        self.assertEqual(self.assignments._giftees[0].name, "Lilo")

    def test_third_giftee(self):
        self.assertEqual(self.assignments._giftees[2].name, "Monk")

    def test_create_participants(self):
        self.assertEqual(self.participant_names, self.assignments.get_giftees_names())

    def test_check_giving_gift_to_myself(self):
        self.assertTrue(
            self.assignments.deny_giving_gift_to_myself()
        )

    def test_check_for_reciprocity(self):
        self.assignments.deny_for_reciprocity()
