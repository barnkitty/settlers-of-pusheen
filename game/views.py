from django.shortcuts import render
from .models import Resource


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_resources = Resource.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_resources},
    )
