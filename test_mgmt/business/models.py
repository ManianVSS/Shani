from django.db import models

from api.models import OrgModel, OrgGroup, ReviewStatus
from api.storage import CustomFileSystemStorage


class Attachment(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='business_attachments')
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='business', blank=False, null=False)


class Tag(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='business_tags')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class RequirementCategory(OrgModel):
    class Meta:
        verbose_name_plural = "requirement categories"

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='business_requirement_categories')
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='sub_categories')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name='sub_categories', blank=True)
    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='business', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='requirement_category_attachments', blank=True)


class Requirement(OrgModel):
    # The status of a step's test design
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='business_requirements')
    parent = models.ForeignKey(RequirementCategory, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='requirements', verbose_name='category')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=11, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    tags = models.ManyToManyField(Tag, related_name='requirements', blank=True)
    external_id = models.CharField(max_length=256, blank=True, null=True)

    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='requirements', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='requirement_attachments', blank=True)
