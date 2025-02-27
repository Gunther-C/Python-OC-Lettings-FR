from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class TestIntegrationProfiles(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='gunther', password='password')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profiles_index_view(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, 'Profiles')
        self.assertContains(response, 'gunther')
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_view(self):
        response = self.client.get(reverse('profiles:profile', args=['gunther']))
        self.assertContains(response, 'gunther')
        self.assertContains(response, 'Paris')
        self.assertEqual(response.status_code, 200)
