from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django_yaml_field import YAMLField

from api.models import OrgModel, OrgGroup, GherkinField
from api.storage import CustomFileSystemStorage
from execution import ipte_util


class Attachment(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='execution_attachments')
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='execution', blank=False, null=False)


class Tag(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='execution_tags')
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Release(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='execution_releases')
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    properties = YAMLField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='release_attachments', blank=True)


class Build(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='execution_builds')
    release = models.ForeignKey(Release, null=True, blank=True, on_delete=models.SET_NULL, related_name='builds')
    name = models.CharField(max_length=256, )
    type = models.CharField(max_length=256, null=True, blank=True)
    build_time = models.DateTimeField(null=True, blank=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    properties = YAMLField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='build_attachments', blank=True)


class Defect(OrgModel):
    release = models.ForeignKey(Release, null=True, blank=True, on_delete=models.SET_NULL, related_name='defects')
    build = models.ForeignKey(Build, null=True, blank=True, on_delete=models.SET_NULL, related_name='defects')
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    external_id = models.CharField(max_length=50, blank=True)
    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='execution', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='defect_attachments', blank=True)


class Run(OrgModel):
    release = models.ForeignKey(Release, null=True, blank=True, on_delete=models.SET_NULL, related_name='runs')
    build = models.ForeignKey(Build, null=True, blank=True, on_delete=models.SET_NULL, related_name='runs')
    name = models.CharField(max_length=256, )
    start_time = models.DateTimeField(verbose_name='start time', null=True, blank=True)
    end_time = models.DateTimeField(verbose_name='end time', null=True, blank=True)


class ExecutionRecordStatus(models.TextChoices):
    PENDING = 'PENDING', _('Pending execution'),
    PASS = 'PASS', _('Passed'),
    FAILED = 'FAILED', _('Failed'),


class ExecutionRecord(OrgModel):
    run = models.ForeignKey(Run, null=True, on_delete=models.SET_NULL, related_name='execution_records')
    name = models.CharField(max_length=256)
    start_time = models.DateTimeField(verbose_name='start time', null=True, blank=True)
    end_time = models.DateTimeField(verbose_name='end time', null=True, blank=True)

    summary = models.CharField(max_length=256, null=True, blank=True)
    description = GherkinField(null=True, blank=True)

    status = models.CharField(max_length=8, choices=ExecutionRecordStatus.choices,
                              default=ExecutionRecordStatus.PENDING)

    defects = models.ManyToManyField(Defect, related_name='execution_records', blank=True)


class ReliabilityRun(OrgModel):
    class ReliabilityRunType(models.TextChoices):
        GROWTH = 'GROWTH', _('Growth'),
        LONGEVITY = 'LONGEVITY', _('Longevity'),
        CHAOS = 'CHAOS', _('Choas'),
        DEMONSTRATION = 'DEMONSTRATION', _('Demonstration'),

    class ReliabilityRunStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending execution'),
        IN_PROGRESS = 'IN_PROGRESS', _('In progress'),
        COMPLETED = 'COMPLETED', _('Completed'),

    release = models.ForeignKey(Release, null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='reliability_runs')

    build = models.ForeignKey(Build, null=True, blank=True, on_delete=models.SET_NULL, related_name='reliability_runs')
    name = models.CharField(max_length=256, null=True, blank=True)
    type = models.CharField(max_length=13, choices=ReliabilityRunType.choices, default=ReliabilityRunType.GROWTH)

    start_time = models.DateTimeField(verbose_name='start time', null=True, blank=True)
    modified_time = models.DateTimeField(verbose_name='modified time', null=True, blank=True)

    testName = models.CharField(max_length=200, null=True, blank=True, verbose_name='test name')
    testEnvironmentType = models.CharField(max_length=200, null=True, blank=True, verbose_name='test environment type')
    testEnvironmentName = models.CharField(max_length=200, null=True, blank=True, verbose_name='test environment name')

    status = models.CharField(max_length=11, choices=ReliabilityRunStatus.choices, default=ReliabilityRunStatus.PENDING)

    totalIterationCount = models.IntegerField(null=True, blank=True, verbose_name='total iteration count')
    passedIterationCount = models.IntegerField(null=True, blank=True, verbose_name='passed iteration count')
    incidentCount = models.IntegerField(null=True, blank=True, verbose_name='incident count')
    targetIPTE = models.FloatField(null=True, blank=True, verbose_name='target IPTE')
    ipte = models.FloatField(null=True, blank=True, verbose_name='IPTE')

    def __str__(self):
        return str(self.name) + ": " + str(self.testName) + ": " + str(
            self.release.name if self.release else "<unknown release>") + ": " + str(self.build)

    # noinspection PyTypeChecker
    def recalculate_ipte(self):
        self.ipte = -1.0
        if self.incidentCount and self.totalIterationCount:
            if self.totalIterationCount > 0:
                self.ipte = ipte_util.calculate_ipte(self.totalIterationCount, self.incidentCount)


class ReliabilityIteration(OrgModel):
    class ReliabilityIterationStatus(models.TextChoices):
        IN_PROGRESS = 'IN_PROGRESS', _('In progress'),
        PASSED = 'PASSED', _('Passed'),
        FAILED = 'FAILED', _('Failed'),
        ERROR = 'ERROR', _('Error'),

    run = models.ForeignKey(ReliabilityRun, null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='reliability_iterations')
    name = models.CharField(max_length=256, )
    index = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=11, choices=ReliabilityIterationStatus.choices,
                              default=ReliabilityIterationStatus.IN_PROGRESS)
    start_time = models.DateTimeField(verbose_name='start time', null=True, blank=True)
    end_time = models.DateTimeField(verbose_name='end time', null=True, blank=True)
    results = models.JSONField(null=True, blank=True)

    def __str__(self):
        return (self.run.name if self.run else "") + ":" + str(self.name) + ":" + str(self.index)


class ReliabilityIncident(OrgModel):
    release = models.ForeignKey(Release, null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='reliability_incidents')
    build = models.ForeignKey(Build, null=True, blank=True, on_delete=models.SET_NULL,
                              related_name='reliability_incidents')
    run = models.ForeignKey(ReliabilityRun, null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='reliability_incidents')
    iteration = models.ForeignKey(ReliabilityIteration, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name='reliability_incidents')
    defect = models.ForeignKey(Defect, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='reliability_incidents')
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    triaged = models.BooleanField(default=False)
    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='execution', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='reliability_incidents', blank=True)


class Environment(OrgModel):
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    type = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name='assigned for user', related_name='environments')
    purpose = models.CharField(max_length=1024, null=True, blank=True)
    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='execution', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='environment_attachments', blank=True)
    current_release = models.ForeignKey(Release, null=True, blank=True, on_delete=models.SET_NULL,
                                        related_name='environments', verbose_name='currently installed release')
    current_build = models.ForeignKey(Build, null=True, blank=True, on_delete=models.SET_NULL,
                                      related_name='environments', verbose_name='currently installed build')
    properties = YAMLField(null=True, blank=True)

    def get_list_query_set(self, user):
        if user.is_superuser:
            return self.objects.all()
        user_id = user.id if user else None
        return self.objects.filter(Q(org_group__isnull=True)
                                   | Q(org_group__members__pk=user_id)
                                   | Q(org_group__leaders__pk=user_id)
                                   ).distinct()

    def can_read(self, user):
        return self.is_owner(user) or self.is_member(user)


model_name_map = {
    'Attachment': Attachment,
    'Tag': Tag,
    'Release': Release,
    'Build': Build,
    'Defect': Defect,
    'Run': Run,
    'ExecutionRecord': ExecutionRecord,
    'ReliabilityIncident': ReliabilityIncident,
    'ReliabilityRun': ReliabilityRun,
    'ReliabilityIteration': ReliabilityIteration,
    'Environment': Environment,
}
