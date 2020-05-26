from django.shortcuts import HttpResponseRedirect

class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        test = response.status_code

        """ if test == 403:
            print("unauthorized")
            return HttpResponsePermanentRedirect('user_app:login')
        else: 
            return self.get_response(request) """

        if test == 403:
            return HttpResponseRedirect('login')


        # Code to be executed for each request/response after
        # the view is called.
        print("response", response)
        print("test", test)
        return response

    