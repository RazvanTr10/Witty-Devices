from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return to the index page """

    return render(request, 'home/index.html')

def privacy_policy(request):
    """
    A view to render the privacy policy page
    """
    return render(request, "home/privacy_policy.html")

