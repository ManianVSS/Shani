import io
from http import HTTPStatus

import cv2
import pyotp
import qrcode
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy

from api.models import OrgModel, OrgGroup
from api.storage import CustomFileSystemStorage
from requirements.models import Feature


class Attachment(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='automation_attachments')
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='automation', blank=False, null=False)


class Tag(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='automation_tags')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


# TODO: Add Automation Feature and Scenario

class Step(OrgModel):
    # The status of a step's automation
    class StepAutomationStatus(models.TextChoices):
        NOT_AUTOMATED = 'NOT_AUTOMATED', gettext_lazy('Not Automated'),
        IN_PROGRESS = 'IN_PROGRESS', gettext_lazy('In Progress'),
        IN_REVIEW = 'IN_REVIEW', gettext_lazy('In Review'),
        ACCEPTED = 'ACCEPTED', gettext_lazy('Accepted'),

    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='steps', null=True, blank=True)

    name = models.CharField(max_length=1024, unique=True)
    summary = models.CharField(max_length=1024, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    eta = models.FloatField(null=True, blank=True, verbose_name='estimated time to execute')
    tags = models.ManyToManyField(Tag, related_name='steps', blank=True)
    status = models.CharField(max_length=13, choices=StepAutomationStatus.choices,
                              default=StepAutomationStatus.NOT_AUTOMATED, verbose_name='automation status')
    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='automation', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='step_attachments', blank=True)


class Properties(OrgModel):
    class Meta:
        verbose_name_plural = "properties"

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='api_properties')
    name = models.CharField(max_length=256)
    details = models.TextField(null=True, blank=True)


class MockAPI(OrgModel):
    class HTTPMethod(models.TextChoices):
        GET = 'GET', gettext_lazy('GET'),
        PUT = 'PUT', gettext_lazy('PUT'),
        POST = 'POST', gettext_lazy('POST'),
        PATCH = 'PATCH', gettext_lazy('PATCH'),
        DELETE = 'DELETE', gettext_lazy('DELETE'),
        ALL = 'ALL', gettext_lazy('All methods'),

    class ContentType(models.TextChoices):
        APPLICATION_JSON = 'application/json', gettext_lazy('JSON'),
        APPLICATION_XML = 'application/xml', gettext_lazy('XML'),
        APPLICATION_OCTET_STREAM = 'application/octet-stream', gettext_lazy('binary'),
        TEXT_HTML = 'text/html', gettext_lazy('HTML'),
        TEXT_PLAIN = 'text/plain', gettext_lazy('Text'),

    name = models.CharField(max_length=1024, unique=True)
    summary = models.CharField(max_length=1024, null=True, blank=True)
    status = models.IntegerField(choices=[(s.value, s.name) for s in HTTPStatus].append((430, "CUSTOM_ERROR_CODE")),
                                 default=200, max_length=32)
    content_type = models.CharField(max_length=32, choices=ContentType.choices, default=ContentType.APPLICATION_JSON)
    body = models.TextField(null=True, blank=True)
    http_method = models.CharField(max_length=32, choices=HTTPMethod.choices, default=HTTPMethod.ALL)


class AuthenticatorSecret(OrgModel):
    user = models.CharField(max_length=256, null=True, blank=True)
    secret = models.CharField(max_length=256, null=True, blank=True)
    issuer = models.CharField(max_length=256, null=True, blank=True)
    url = models.CharField(max_length=1024, null=True, blank=True)
    qr_code = models.ImageField(storage=CustomFileSystemStorage, upload_to='automation', blank=True, null=True,
                                verbose_name='QR-Code image file in PNG format')
    initialized = models.BooleanField(default=False, verbose_name='is already initialized')


@receiver(post_save, sender=AuthenticatorSecret, dispatch_uid="update_authenticator_secret")
def update_authenticator_secret(sender, instance, **kwargs):
    if instance is not None:
        if not instance.initialized:
            if (instance.qr_code is not None) and (instance.qr_code.name is not None):
                image = cv2.imread(instance.qr_code.path)
                # initialize the cv2 QRCode detector
                detector = cv2.QRCodeDetector()
                data, bbox, straight_qrcode = detector.detectAndDecode(image)

                if bbox is not None:
                    instance.url = data
                    instance.initialized = True
                    instance.save()
            elif instance.url is not None:
                otp_object = pyotp.parse_uri(instance.url)
                if instance.user is None:
                    instance.user = otp_object.name
                if instance.secret is None:
                    instance.secret = otp_object.secret
                if instance.issuer is None:
                    instance.issuer = otp_object.issuer
                image = qrcode.make(instance.url)
                buf = io.BytesIO()
                image.save(buf, "PNG")
                contents = buf.getvalue()
                content_file = ContentFile(contents, name="AuthenticationSecretQRCode-" + str(instance.id) + ".png")
                instance.qr_code = content_file
                instance.initialized = True
                instance.save()
            elif (instance.user is not None) and (instance.secret is not None) and (instance.issuer is not None):
                otp_object = pyotp.totp.TOTP(instance.secret).provisioning_uri(name=instance.user,
                                                                               issuer_name=instance.issuer)
                instance.url = str(otp_object)
                # instance.url = 'otpauth://totp/' + urllib.parse.quote_plus(
                #     instance.user) + '?secret=' + urllib.parse.quote_plus(
                #     instance.secret) + '&issuer=' + urllib.parse.quote_plus(
                #     instance.issuer)
                image = qrcode.make(instance.url)

                buf = io.BytesIO()
                image.save(buf, "PNG")
                contents = buf.getvalue()
                content_file = ContentFile(contents, name="AuthenticationSecretQRCode-" + str(instance.id) + ".png")
                instance.qr_code = content_file
                instance.initialized = True
                instance.save()

# class StepInstance:
#     def __init__(self, step, data):
#         self.step = step if step else "<unnamed>"
#         self.data = data if data else {}
#
#     def __str__(self):
#         return str(self.step)
#
#
# class ScenarioInstance:
#
#     def __init__(self, step, data):
#         self.name = models.CharField(max_length=1024, unique=True)
#         self.summary = models.CharField(max_length=1024, null=True, blank=True)
#         self.data = models.JSONField(null=True, blank=True)
#
#     def __str__(self):
#         return '[' + str(self.name) + ']: ' + str(self.summary)
