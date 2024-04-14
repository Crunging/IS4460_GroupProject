from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import resolve

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Exclude paths from requiring login (e.g., admin, login, logout)
        if request.path.startswith('/admin/') or request.path.startswith('/login/') or request.path.startswith('/logout/'):
            return None

        # Apply login required except for the login and logout views
        if not request.user.is_authenticated:
            return login_required(view_func)(request, *view_args, **view_kwargs)
        return None
