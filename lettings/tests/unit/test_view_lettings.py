from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class TestViewLettings(TestCase):
    """
    Test case for the views in the Letting app.
    Cas de test pour les vues de l'application Letting.
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

    def test_lettings_index_template(self):
        """
        Test that the lettings index view uses the correct template.
        Tester que la vue index des lettings utilise le bon template.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_template(self):
        """
        Test that the letting detail view uses the correct template.
        Tester que la vue détaillée du letting utilise le bon template.
        """
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.status_code, 200)
