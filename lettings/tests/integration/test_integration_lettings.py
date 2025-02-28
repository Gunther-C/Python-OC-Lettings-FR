from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class TestIntegrationLettings(TestCase):
    """
    Test case for the integration of the Letting app.
    Cas de test pour l'intégration de l'application Letting.
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

    def test_lettings_index_view(self):
        """
        Test that the lettings index view displays correctly.
        Tester que la vue index des lettings s'affiche correctement.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, 'Lettings')
        self.assertContains(response, 'Terrain de campagne')
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_view(self):
        """
        Test that the letting detail view displays correctly.
        Tester que la vue détaillée du letting s'affiche correctement.
        """
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertContains(response, 'Terrain de campagne')
        self.assertContains(response, 'Le Chemin')
        self.assertEqual(response.status_code, 200)
