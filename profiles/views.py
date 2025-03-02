from django.shortcuts import render
from .models import Profile
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the profiles index view with the list of profiles.
    Rend la vue index des profiles avec la liste des profiles.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered profiles index view.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    logger.info("Fetched all profiles.")
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Renders the profile detail view for a specific user.
    Rend la vue détaillée du profile pour un utilisateur spécifique.
    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the profile to retrieve.
    Returns:
        HttpResponse: The rendered profile detail view.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Successfully fetched profile for user: {username}")
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.error(f"Profile for user {username} does not exist.", exc_info=True)
