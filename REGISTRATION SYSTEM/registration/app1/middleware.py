from django.shortcuts import redirect
from django.urls import reverse

class PreventLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == reverse('login'):
            return redirect('home')  # Redirect to the home page
        return self.get_response(request)
