import unittest
from src.commands import add_contact

class TestBotFunctions(unittest.TestCase):
    def setUp(self):
        self.contacts = {}

    def test_add_contact(self):
        result = add_contact(["Ivan", "12345"], self.contacts)
        self.assertEqual(result, "Contact added.")
        self.assertIn("Ivan", self.contacts)
        self.assertEqual(self.contacts["Ivan"], "12345")

    def test_add_contact_invalid_phone(self):
        result = add_contact(["Ivan", "abc123"], self.contacts)
        self.assertEqual(result, "Phone number must contain only digits.")
        self.assertNotIn("Ivan", self.contacts)

if __name__ == "__main__":
    unittest.main()
