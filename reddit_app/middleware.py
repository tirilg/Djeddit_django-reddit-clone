import re
from django.shortcuts import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.shortcuts import redirect



class IPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ip_addresses = ['127.0.0.1']
        client_ip_address = request.META.get('REMOTE_ADDR')

        if not client_ip_address in allowed_ip_addresses:
            raise PermissionDenied

        response = self.get_response(request)
        return response

    
AUTH_URLS = []

if hasattr(settings, 'AUTH_URLS'):
    AUTH_URLS += [re.compile(url) for url in settings.AUTH_URLS]


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')

        if not request.user.is_authenticated:
            if any(url.match(path) for url in AUTH_URLS):
                return redirect(settings.LOGIN_URL)
