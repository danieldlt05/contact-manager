# test_contact_manager.py

import unittest
from contact_manager import add_contact, find_contact, delete_contact, contacts, DuplicateContactError

class TestContactManager(unittest.TestCase):

    def setUp(self):
        """Reset contacts before each test."""
        contacts.clear()

    def test_add_new_contact(self):
        add_contact("Dan", "12345")
        self.assertIn("Dan", contacts)
        self.assertEqual(contacts["Dan"], "12345")

    def test_find_existing_contact(self):
        contacts["Joe"] = "67890"
        self.assertEqual(find_contact("Joe"), "67890")
    
    def test_find_nonexistent_contact(self):
        with self.assertRaises(KeyError):
            find_contact("Justin")

    def test_delete_existing_contact(self):
        contacts["Diego"] = "55555"
        delete_contact("Diego")
        self.assertNotIn("Diego", contacts)

    def test_delete_nonexistent_contact(self):
        with self.assertRaises(KeyError):
            delete_contact("Jesus")

    def test_add_duplicate_contact(self):
        add_contact("Tyler", "11111")
        with self.assertRaises(DuplicateContactError):
            add_contact("Tyler", "22222")

if __name__ == "__main__":
    unittest.main()
