from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class TestViewProfiles(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='gunther', password='password')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profiles_index_template(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_template(self):
        response = self.client.get(reverse('profiles:profile', args=['gunther']))
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.status_code, 200)
