

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return self.name + ' ' + self.surname


class Group:

    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group('TODO', self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        all_names = ', '.join(map(str, self.people))
        return f'Group {self.name} with members {all_names}'

    def __getitem__(self, key: int):
        return f"Person {key}: {self.people[key]}"


# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
#
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
#
# # print(len(first_group))
# # print(second_group)
# # print(third_group[0])
#
# for person in third_group:
#     print(person)


import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Stefan", "Dimitrov")

    def test_custom_repr(self):
        result = repr(self.person_1)
        self.assertIn("Stefan", result)
        self.assertEqual(result, "Stefan Dimitrov")

    def test_custom_str(self):
        result = str(self.person_1)
        self.assertIn("Stefan", result)
        self.assertNotIn("Person", result)
        self.assertEqual(result, "Stefan Dimitrov")

    def test_custom_add(self):
        person_2 = Person("Test", "Testov")
        person_3 = self.person_1 + person_2
        self.assertEqual(person_3.name, "Stefan")
        self.assertEqual(person_3.surname, "Testov")

    def test_set_attributes(self):
        self.assertEqual(self.person_1.name, "Stefan")
        self.assertEqual(self.person_1.surname, "Dimitrov")


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Stefan", "Dimitrov")
        self.person_2 = Person("Second", "Person")
        self.group = Group("test", [self.person_1, self.person_2])

    def test_custom_len(self):
        result = len(self.group)
        self.assertEqual(result, 2)

    def test_custom_add(self):
        person_3 = Person("Third", "Third")
        group_2 = Group("test2", [person_3])
        group_3 = self.group + group_2
        self.assertEqual(len(group_3), 3)

    def test_custom_get_item(self):
        result = self.group[1]
        self.assertIn("Second", result)
        self.assertEqual(result,"Person 1: Second Person")


    def test_custom_get_item_invalid_index(self):
        with self.assertRaises(IndexError):
            result = self.group[2]

    def test_custom_repr(self):
        result = repr(self.group)
        # self.assertIn("Group", result)
        # self.assertIn("Stefan", result)
        # self.assertIn("Second", result)
        self.assertEqual(result, "Group test with members Stefan Dimitrov, Second Person")

    def test_custom_str(self):
        result = str(self.group)
        # self.assertIn("Group", result)
        # self.assertIn("Stefan", result)
        # self.assertIn("Second", result)
        self.assertEqual(result, "Group test with members Stefan Dimitrov, Second Person")

    def test_set_attributes(self):
        self.assertEqual(self.group.name, "test")
        self.assertEqual(len(self.group.people), 2)


if __name__ == "__main__":
    unittest.main()
