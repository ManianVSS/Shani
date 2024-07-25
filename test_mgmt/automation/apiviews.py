import pyotp
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AuthenticatorSecret
from .serializers import AuthenticatorSecretSerializer


@api_view(['GET'])
def generate_otp(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    authenticator_secret_id = None
    if 'authenticator_secret' in request.GET:
        authenticator_secret_id = request.query_params.get('authenticator_secret')
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, content='Missing parameter authenticator_secret')
    try:
        authenticator_secret = AuthenticatorSecret.objects.get(
            pk=authenticator_secret_id) if authenticator_secret_id else None
    except AuthenticatorSecret.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='Could not find authenticator secret passed')

    otp_object = pyotp.parse_uri(authenticator_secret.url)
    return_object = AuthenticatorSecretSerializer(authenticator_secret).data
    return_object['otp'] = otp_object.now()
    return Response(return_object)
