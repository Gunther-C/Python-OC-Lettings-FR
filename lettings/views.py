from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Renders the index view with the list of lettings.
    Rend la vue index avec la liste des letings.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered index view.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Renders the letting detail view for a specific letting.
    Rend la vue détaillée du letting pour un letting spécifique.
    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to retrieve.
    Returns:
        HttpResponse: The rendered letting detail view.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
