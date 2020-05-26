from django.shortcuts import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print("request", request)
        test = response.status_code

        """ if not request.user.is_authenticated:
            print("hi")
            return HttpResponseRedirect("/user/login/") """
        """ 
        if test == 403:
            return HttpResponseRedirect("/user/login/") """

        """ if test == 403:
            print("unauthorized")
            return HttpResponsePermanentRedirect('user_app:login')
        else: 
            return self.get_response(request) """


        # Code to be executed for each request/response after
        # the view is called.
        return response



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

    