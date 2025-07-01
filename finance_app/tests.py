from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class FinanceAppTestCase(TestCase):
    def test_home_page(self):
        """Test that the home page loads successfully"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_sip_calculator_page(self):
        """Test that the SIP calculator page loads successfully"""
        response = self.client.get(reverse('sip_calculator'))
        self.assertEqual(response.status_code, 200)
    
    def test_fd_and_rd_page(self):
        """Test that the FD and RD page loads successfully"""
        response = self.client.get(reverse('fd_and_rd'))
        self.assertEqual(response.status_code, 200)
