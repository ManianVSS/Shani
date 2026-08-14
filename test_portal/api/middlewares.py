class CustomCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"

        # Code to be executed for each request/response after
        # the view is called.

        return response


class StripInsecureCoopMiddleware:
    def __init__(self, get_response):
        self.TRUSTED_HOSTS = ["*"]
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        host = request.get_host().split(":", 1)[0]

        # Allow insecure COOP for trusted hosts or secure requests.
        is_trusted = request.is_secure() or '*' in self.TRUSTED_HOSTS or host in self.TRUSTED_HOSTS

        if not is_trusted and "Cross-Origin-Opener-Policy" in response:
            response.pop("Cross-Origin-Opener-Policy", None)

        return response
