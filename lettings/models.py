from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address in the system.
    Représente une adresse dans le système.

    Attributes:
        number (PositiveIntegerField): The number of the address, validated to be less than 9999.
        street (CharField): The street of the address.
        city (CharField): The city of the address.
        state (CharField): The state of the address, validated to have exactly 2 characters.
        zip_code (PositiveIntegerField): The postal code of the address, validated to be less than 99999.
        country_iso_code (CharField): The ISO country code of the address, validated to have exactly 3 characters.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
        Represents a letting in the system.
        Représente une location dans le système.

        Attributes:
            title (CharField): The title of the letting.
            address (OneToOneField): The address associated with the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="letting")

    class Meta:
        verbose_name = 'letting'
        verbose_name_plural = 'lettings'

    def __str__(self):
        return self.title
