from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import OrgModel, OrgGroup, ReviewStatus
from requirements.models import UseCase


class Attachment(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='test_attachments')
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to='test_design', blank=False, null=False)

    def __str__(self):
        return str(self.file.name)


class Tag(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='test_tags')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


# Create your models here.
class TestCaseCategory(OrgModel):
    class Meta:
        verbose_name_plural = "test case categories"

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='test_testcase_categories')
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='sub_categories')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name='test_categories', blank=True)
    details_file = models.FileField(upload_to='test_design', blank=True, null=True, verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='test_case_category_attachments', blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class TestCase(OrgModel):
    class TestType(models.TextChoices):
        MANUAL = 'MANUAL', _('Manual'),
        AUTOMATABLE = 'AUTOMATABLE', _('Automatable'),
        AUTOMATED = 'AUTOMATED', _('Automated'),

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='test_testcases')
    parent = models.ForeignKey(TestCaseCategory, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='testcases', verbose_name='test case category')

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=11, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)
    type = models.CharField(max_length=11, choices=TestType.choices, default=TestType.MANUAL)

    tags = models.ManyToManyField(Tag, related_name='test_cases', blank=True)
    external_id = models.CharField(max_length=256, blank=True, null=True)

    details_file = models.FileField(upload_to='test_design', blank=True, null=True, verbose_name='File with details')
    use_cases = models.ManyToManyField(UseCase, related_name='test_cases', blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='test_case_attachments', blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)
