from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy

from api.models import Tag, OrgModel, OrgGroup
from requirements.models import Feature


class Attachment(OrgModel):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to='automation', blank=False, null=False)
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='automation_attachments')


class Step(OrgModel):
    # The status of a step's test design
    class StepDesignStatus(models.TextChoices):
        DRAFT = 'DRAFT', gettext_lazy('Draft'),
        IN_REVIEW = 'IN_REVIEW', gettext_lazy('In Review'),
        ACCEPTED = 'ACCEPTED', gettext_lazy('Accepted'),

    # The status of a step's automation
    class StepAutomationStatus(models.TextChoices):
        NOT_AUTOMATED = 'NOT_AUTOMATED', gettext_lazy('Not Automated'),
        IN_PROGRESS = 'IN_PROGRESS', gettext_lazy('In Progress'),
        IN_REVIEW = 'IN_REVIEW', gettext_lazy('In Review'),
        ACCEPTED = 'ACCEPTED', gettext_lazy('Accepted'),

    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='steps', null=True, blank=True)

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    expected_results = models.TextField(null=True, blank=True, verbose_name="expected results")
    eta = models.FloatField(null=True, blank=True, verbose_name='estimated time to execute')
    tags = models.ManyToManyField(Tag, related_name='steps', blank=True)

    test_design_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='step_test_owners',
                                          verbose_name='test design owner', null=True, blank=True)

    test_design_status = models.CharField(max_length=9, choices=StepDesignStatus.choices,
                                          default=StepDesignStatus.DRAFT, verbose_name='test design status')

    automation_status = models.CharField(max_length=13, choices=StepAutomationStatus.choices,
                                         default=StepAutomationStatus.NOT_AUTOMATED, verbose_name='automation status')

    automation_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='step_automation_owners',
                                         verbose_name='automation owner', null=True, blank=True)

    automation_code_reference = models.TextField(null=True, blank=True)

    details_file = models.FileField(upload_to='automation', blank=True, null=True, verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='step_attachments', blank=True)

    def is_owner(self, user):
        return (user == self.test_design_owner) or (
                (self.feature is not None) and hasattr(self.feature, 'is_owner') and self.feature.is_owner(
            user)) or super().is_owner(user)

    def is_member(self, user):
        return (user == self.automation_owner) or (
                (self.feature is not None) and hasattr(self.feature, 'is_member') and self.feature.is_member(user))
