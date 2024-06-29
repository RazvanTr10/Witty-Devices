from django.shortcuts import render


def index(request):
    """ A view to return to the index page """

    return render(request, 'home/index.html')

def privacy_policy(request):
    """
    A view to render the privacy policy page
    """
    return render(request, "home/privacy_policy.html")

def terms_and_conditions(request):
    """ A view to render the terms and conditions page """

    return render(request, 'home/terms_and_conditions.html')

