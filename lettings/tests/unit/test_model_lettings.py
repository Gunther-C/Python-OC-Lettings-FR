from django.test import TestCase
from lettings.models import Letting, Address

class TestModelLettings(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Le Chemin',
            city='Agde',
            state='CH',
            zip_code=34300,
            country_iso_code='FR'
        )
        self.letting = Letting.objects.create(title='Terrain de campagne', address=self.address)

    def test_address_content(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.street, 'Le Chemin')
        self.assertEqual(address.city, 'Agde')
        self.assertEqual(address.state, 'CH')
        self.assertEqual(address.zip_code, 34300)
        self.assertEqual(address.country_iso_code, 'FR')

    def test_letting_content(self):
        letting = Letting.objects.get(id=1)
        self.assertEqual(letting.title, 'Terrain de campagne')
        self.assertEqual(letting.address, self.address)
