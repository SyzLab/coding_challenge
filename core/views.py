from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    """
    Home page view - accessible to everyone.
    Shows a welcome message and login status.
    """
    return render(request, 'core/home.html')


@login_required
def profile(request):
    """
    User profile view - requires authentication.
    Displays the logged-in user's information.
    """
    return render(request, 'core/profile.html', {
        'user': request.user
    })
