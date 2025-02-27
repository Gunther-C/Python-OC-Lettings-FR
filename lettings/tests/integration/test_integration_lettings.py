from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address

class TestIntegrationLettings(TestCase):
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

    def test_lettings_index_view(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, 'Lettings')
        self.assertContains(response, 'Terrain de campagne')
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_view(self):
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertContains(response, 'Terrain de campagne')
        self.assertContains(response, 'Le Chemin')
        self.assertEqual(response.status_code, 200)
