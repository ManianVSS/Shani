from django.db import models

from api.models import OrgModel, OrgGroup, ReviewStatus


class Attachment(OrgModel):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to='requirements', blank=False, null=False)
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='requirement_attachments')


class Tag(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='requirement_tags')


class FeatureCategory(OrgModel):
    class Meta:
        verbose_name_plural = "feature categories"

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='sub_categories')
    tags = models.ManyToManyField(Tag, related_name='feature_categories', blank=True)
    details_file = models.FileField(upload_to='requirements', blank=True, null=True, verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='feature_category_attachments', blank=True)
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='feature_categories')


class Feature(OrgModel):
    # The status of a step's test design
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    parent = models.ForeignKey(FeatureCategory, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='features', verbose_name='feature category')
    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=11, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    tags = models.ManyToManyField(Tag, related_name='features', blank=True)
    external_id = models.CharField(max_length=256, blank=True, null=True)

    details_file = models.FileField(upload_to='requirements', blank=True, null=True, verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='test_case_attachments', blank=True)

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='requirement_features')


class UseCase(OrgModel):
    feature = models.ForeignKey(Feature, on_delete=models.SET_NULL, null=True, blank=True, related_name="use_cases")

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=11, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    weight = models.FloatField(default=1)
    consumer_score = models.FloatField(default=0, verbose_name='consumer score')
    serviceability_score = models.FloatField(default=0, verbose_name='serviceability score')
    test_confidence = models.FloatField(default=0, verbose_name='test confidence')
    development_confidence = models.FloatField(default=0, verbose_name='development confidence')
    details_file = models.FileField(upload_to='requirements', blank=True, null=True, verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='use_case_attachments', blank=True)

    def get_score(self):
        return (self.consumer_score + self.serviceability_score + self.test_confidence + self.development_confidence) \
            / 4


class Requirement(OrgModel):
    use_cases = models.ManyToManyField(UseCase, related_name='requirements', blank=True)

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
