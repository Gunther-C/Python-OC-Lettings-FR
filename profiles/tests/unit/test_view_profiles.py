from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class TestViewProfiles(TestCase):
    """
    Test case for the views in the Profiles app.
    Cas de test pour les vues de l'application Profiles.
    """
    def setUp(self):
        """
        Set up the test case with a User and Profile instance.
        Configurer le cas de test avec une instance User et Profile.
        """
        self.user = User.objects.create(username='gunther', password='password')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profiles_index_template(self):
        """
        Test that the profiles index view uses the correct template.
        Tester que la vue index des profiles utilise le bon template.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_template(self):
        """
        Test that the profile detail view uses the correct template.
        Tester que la vue détaillée du profile utilise le bon template.
        """
        response = self.client.get(reverse('profiles:profile', args=['gunther']))
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.status_code, 200)
