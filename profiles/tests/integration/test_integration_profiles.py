from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class TestIntegrationProfiles(TestCase):
    """
    Test case for the integration of the Profiles app.
    Cas de test pour l'intégration de l'application Profiles.
    """
    def setUp(self):
        """
        Set up the test case with a User and Profile instance.
        Configurer le cas de test avec une instance User et Profile.
        """
        self.user = User.objects.create(username='gunther', password='password')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profiles_index_view(self):
        """
        Test that the profiles index view displays correctly.
        Tester que la vue index des profiles s'affiche correctement.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, 'Profiles')
        self.assertContains(response, 'gunther')
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_view(self):
        """
        Test that the profile detail view displays correctly.
        Tester que la vue détaillée du profile s'affiche correctement.
        """
        response = self.client.get(reverse('profiles:profile', args=['gunther']))
        self.assertContains(response, 'gunther')
        self.assertContains(response, 'Paris')
        self.assertEqual(response.status_code, 200)
