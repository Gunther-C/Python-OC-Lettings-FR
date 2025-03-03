from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
        Represents a user profile in the system.
        Représente un profil utilisateur dans le système.

        Attributes:
            user (OneToOneField): A one-to-one relationship to the Django User model.
            bio (TextField): A brief biography of the user.
            location (CharField): The location of the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.user.username
