from django.test import TestCase
from lettings.models import Letting, Address


class TestModelLettings(TestCase):
    """
    Test case for the Letting model and its associated Address.
    Cas de test pour le modèle Letting et son adresse associée.
    """
    def setUp(self):
        """
        Set up the test case with an Address and Letting instance.
        Configurer le cas de test avec une instance Address et Letting.
        """
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
        """
        Test that the Address instance contains the correct content.
        Tester que l'instance Address contient le contenu correct.
        """
        address = Address.objects.get(id=1)
        self.assertEqual(address.street, 'Le Chemin')
        self.assertEqual(address.city, 'Agde')
        self.assertEqual(address.state, 'CH')
        self.assertEqual(address.zip_code, 34300)
        self.assertEqual(address.country_iso_code, 'FR')
