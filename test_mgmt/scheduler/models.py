from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_yaml_field import YAMLField

from api.models import OrgModel, OrgGroup
from api.storage import CustomFileSystemStorage


class Attachment(OrgModel):
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='scheduler', blank=False, null=False)


class Tag(OrgModel):
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class ResourceType(OrgModel):
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class ResourceSet(OrgModel):
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='resource_set_attachments', blank=True)


class ResourceSetComponent(OrgModel):
    resource_set = models.ForeignKey(ResourceSet, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='components')
    type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='resource_set_components')

    count = models.IntegerField(default=1)


class RequestStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft'),
    PENDING = 'PENDING', _('Pending'),
    ASSIGNED = 'ASSIGNED', _('Assigned'),
    CLOSED = 'CLOSED', _('Closed'),


class Request(OrgModel):
    requester = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="scheduler_requests")
    name = models.CharField(max_length=256)
    resource_set = models.ForeignKey(ResourceSet, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='requests')
    priority = models.IntegerField(default=255)
    start_time = models.DateTimeField(verbose_name='start time')
    end_time = models.DateTimeField(verbose_name='end time')
    purpose = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=10, choices=RequestStatus.choices, default=RequestStatus.DRAFT)

    attachments = models.ManyToManyField(Attachment, related_name='request_attachments', blank=True)


class Resource(OrgModel):
    type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='resources')
    name = models.CharField(max_length=256, null=True, blank=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    assigned_to = models.ForeignKey(Request, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name='assigned for request', related_name='resources')
    attachments = models.ManyToManyField(Attachment, related_name='resource_attachments', blank=True)
    properties = YAMLField(null=True, blank=True)


model_name_map = {
    'Attachment': Attachment,
    'Tag': Tag,
    'ResourceType': ResourceType,
    'ResourceSet': ResourceSet,
    'ResourceSetComponent': ResourceSetComponent,
    'Request': Request,
    'Resource': Resource,
}
