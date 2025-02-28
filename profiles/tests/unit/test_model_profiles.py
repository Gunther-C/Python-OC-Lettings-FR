from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class TestModelProfiles(TestCase):
    """
    Test case for the Profile model.
    Cas de test pour le modèle Profile.
    """
    def setUp(self):
        """
        Set up the test case with a User and Profile instance.
        Configurer le cas de test avec une instance User et Profile.
        """
        user = User.objects.create(username='gunther', password='password')
        Profile.objects.create(user=user, favorite_city='Paris')

    def test_profile_content(self):
        """
        Test that the Profile instance contains the correct content.
        Tester que l'instance Profile contient le contenu correct.
        """
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.user.username, 'gunther')
        self.assertEqual(profile.favorite_city, 'Paris')
