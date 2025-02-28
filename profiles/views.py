from django.shortcuts import render
from .models import Profile


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
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
