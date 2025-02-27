from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class TestModelProfiles(TestCase):
    def setUp(self):
        user = User.objects.create(username='gunther', password='password')
        Profile.objects.create(user=user, favorite_city='Paris')

    def test_profile_content(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.user.username, 'gunther')
        self.assertEqual(profile.favorite_city, 'Paris')
