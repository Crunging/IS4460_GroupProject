from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path not in [reverse('login'), reverse('logout'), '/admin/']:
                return redirect(settings.LOGIN_URL)
        return self.get_response(request)