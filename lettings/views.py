from django.shortcuts import render
from .models import Letting
import logging

logger = logging.getLogger(__name__)


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
    logger.info("Fetched all lettings.")
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
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        logger.info(f"Successfully fetched letting with ID: {letting_id}")
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.error(f"Letting with ID {letting_id} does not exist.", exc_info=True)
