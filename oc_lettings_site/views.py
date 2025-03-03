from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the index view of the oc_lettings_site.
    Rend la vue index du site oc_lettings_site.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered index view.
    """
    logger.info("Enter index")
    return render(request, 'oc_lettings_site/index.html')


def error_404(request, exception):
    """
    Renders the custom 404 error page.
    Rend la page d'erreur 404 personnalisée.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that caused the 404 error.

    Returns:
        HttpResponse: The rendered 404 error page.
    """
    logger.error(f"Error 404: {exception}")
    return render(request, 'oc_lettings_site/404.html', status=404)


def error_500(request):
    """
    Renders the custom 500 error page.
    Rend la page d'erreur 500 personnalisée.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 500 error page.
    """
    logger.error("Error 500:", exc_info=True)
    return render(request, 'oc_lettings_site/500.html', status=500)
