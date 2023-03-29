from django.contrib.auth.models import User
from django.db import models

from api.models import Tag, OrgModel, OrgGroup, ReviewStatus
from test_mgmt import settings


class Attachment(OrgModel):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to=settings.MEDIA_BASE_NAME, blank=False, null=False)
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='automation_attachments')

    def __str__(self):
        return str(self.file.name)


class FeatureCategory(OrgModel):
    class Meta:
        verbose_name_plural = "feature categories"

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    category = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='sub_categories')

    tags = models.ManyToManyField(Tag, related_name='test_categories', blank=True)
    details_file = models.FileField(upload_to='automation', blank=True, null=True, verbose_name='File with details')

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Feature(OrgModel):
    # The status of a step's test design
    category = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name='features')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='features', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='feature owner', null=True, blank=True)
    status = models.CharField(max_length=11, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)
    details_file = models.FileField(upload_to='automation', blank=True, null=True, verbose_name='File with details')

    def __str__(self):
        return str(self.name)

    def is_owner(self, user):
        return (user == self.owner) or super().is_owner(user)
