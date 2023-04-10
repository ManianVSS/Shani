from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import OrgModel, OrgGroup
from execution import ipte_util


class Attachment(OrgModel):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to='execution', blank=False, null=False)
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='execution_attachments')


class Tag(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='execution_tags')


class Release(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='execution_releases')


class Defect(OrgModel):
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    external_id = models.CharField(max_length=50, blank=True)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='defects')
    details_file = models.FileField(upload_to='execution', blank=True, null=True, verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='defect_attachments', blank=True)


class Run(OrgModel):
    build = models.CharField(max_length=256)
    name = models.CharField(max_length=256, unique=True)
    time = models.DateTimeField(auto_now_add=True)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='runs')


class ExecutionRecordStatus(models.TextChoices):
    PENDING = 'PENDING', _('Pending execution'),
    PASS = 'PASS', _('Passed'),
    FAILED = 'FAILED', _('Failed'),


class ExecutionRecord(OrgModel):
    run = models.ForeignKey(Run, null=True, on_delete=models.SET_NULL, related_name='execution_records')
    time = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=8, choices=ExecutionRecordStatus.choices,
                              default=ExecutionRecordStatus.PENDING)

    acceptance_test = models.BooleanField(default=False, verbose_name='is acceptance test')
    automated = models.BooleanField(default=False, verbose_name='is automated')

    defects = models.ManyToManyField(Defect, related_name='execution_records', blank=True)


class ReliabilityRunStatus(models.TextChoices):
    PENDING = 'PENDING', _('Pending execution'),
    IN_PROGRESS = 'IN_PROGRESS', _('In progress'),
    COMPLETED = 'COMPLETED', _('Completed'),


# noinspection PyTypeChecker
class ReliabilityRun(OrgModel):
    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='reliability_runs')

    build = models.CharField(max_length=256)
    name = models.CharField(max_length=256, null=True, blank=True)

    start_time = models.DateTimeField(auto_now_add=True, verbose_name='start time')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='modified time')

    testName = models.CharField(max_length=200, verbose_name='test name')
    testEnvironmentType = models.CharField(max_length=200, verbose_name='test environment type')
    testEnvironmentName = models.CharField(max_length=200, verbose_name='test environment name')

    status = models.CharField(max_length=11, choices=ReliabilityRunStatus.choices,
                              default=ReliabilityRunStatus.PENDING)

    totalIterationCount = models.IntegerField(null=True, blank=True, verbose_name='total iteration count')
    passedIterationCount = models.IntegerField(null=True, blank=True, verbose_name='passed iteration count')
    incidentCount = models.IntegerField(null=True, blank=True, verbose_name='incident count')
    targetIPTE = models.FloatField(null=True, blank=True, verbose_name='target IPTE')
    ipte = models.FloatField(null=True, blank=True, verbose_name='IPTE')
    incidents = models.ManyToManyField(Defect, related_name='reliability_runs', blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.testName) + ": " + str(self.release.name) + ": " + str(self.build)

    def recalculate_ipte(self):
        self.ipte = -1.0
        if self.incidentCount and self.totalIterationCount:
            if self.totalIterationCount > 0:
                self.ipte = ipte_util.calculate_ipte(self.totalIterationCount, self.incidentCount)


class Environment(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    type = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    purpose = models.CharField(max_length=1024, null=True, blank=True)
    details_file = models.FileField(upload_to='execution', blank=True, null=True, verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='environment_attachments', blank=True)
    current_release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='environments',
                                        verbose_name='currently release')

    def can_read(self, user):
        return self.is_owner(user) or self.is_member(user)
