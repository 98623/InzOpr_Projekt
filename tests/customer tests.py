import unittest
from customer import Customer

#Testy jednostkowe

class TestCustomer(unittest.TestCase):

    def test_customer_initialization(self):
        customer = Customer(1, "Jan", "Kowalski", "jan.kowalski@example.com", "ABC12345")
        self.assertEqual(customer.customer_id, 1)
        self.assertEqual(customer.first_name, "Jan")
        self.assertEqual(customer.last_name, "Kowalski")
        self.assertEqual(customer.email, "jan.kowalski@example.com")
        self.assertEqual(customer.license_number, "ABC12345")

    def test_customer_email_is_string(self):
        customer = Customer(2, "Anna", "Nowak", "anna.nowak@example.com", "XYZ98765")
        self.assertIsInstance(customer.email, str)

    def test_license_number_not_empty(self):
        customer = Customer(3, "Piotr", "Zieliński", "piotr@example.com", "XYZ00011")
        self.assertNotEqual(customer.license_number, "")

#Test integracyjny

    def test_adding_customer_to_list(self):
        customer_list = []
        customer = Customer(4, "Kasia", "Wiśniewska", "kasia@example.com", "JKL11223")
        customer_list.append(customer)

        self.assertEqual(len(customer_list), 1)
        self.assertEqual(customer_list[0].first_name, "Kasia")
