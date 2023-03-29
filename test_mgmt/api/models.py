from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.translation import gettext_lazy as _

from api import ipte_util
from test_mgmt import settings


class OrgGroup(models.Model):
    name = models.CharField(max_length=256, unique=True)
    auth_group = models.OneToOneField(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name="org_group",
                                      verbose_name='authorization group')
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    org_group = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="sub_org_groups", verbose_name='parent organization group')
    leaders = models.ManyToManyField(User, blank=True, related_name="org_group_leaders")
    members = models.ManyToManyField(User, blank=True, related_name="org_group_members")

    def __str__(self):
        return str(self.name)

    def is_owner(self, user):
        # noinspection PyUnresolvedReferences
        return ((self.leaders is not None) and (user in self.leaders.all())) or (
                (self.org_group is not None) and self.org_group.is_owner(user))

    def is_member(self, user):
        # noinspection PyUnresolvedReferences
        return ((self.members is not None) and (user in self.members.all())) or (
                (self.org_group is not None) and self.org_group.is_member(user))


class OrgModel(models.Model):
    class Meta:
        abstract = True

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group')

    def is_owner(self, user):
        if self.org_group is None:
            return False
        is_owner = self.org_group.is_owner(user)
        return is_owner

    def is_member(self, user):
        if self.org_group is None:
            return False
        is_member = self.org_group.is_member(user)
        return is_member


class Attachment(OrgModel):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to=settings.MEDIA_BASE_NAME, blank=False, null=False)

    def __str__(self):
        return str(self.file.name)


class Site(OrgModel):
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='site_attachments', blank=True)

    def __str__(self):
        return str(self.name)


class Engineer(OrgModel):
    employee_id = models.CharField(max_length=20, null=True, unique=True, verbose_name='employee id')
    name = models.CharField(max_length=256, default='<unnamed>')
    auth_user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="engineer",
                                     verbose_name='authorization user')
    role = models.CharField(max_length=256, null=True, blank=True, )
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL,
                             related_name="engineers")
    attachments = models.ManyToManyField(Attachment, related_name='engineer_attachments', blank=True)

    def __str__(self):
        return str(self.auth_user)


class Release(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class EngineerOrgGroupParticipation(OrgModel):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="org_group_participation")
    role = models.CharField(max_length=256, null=True, blank=True, )
    capacity = models.FloatField(default=1.0)

    def __str__(self):
        return str(self.engineer) + " participates in " + str(self.org_group) + " with capacity " + str(
            self.capacity)


class SiteHoliday(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField()
    summary = models.CharField(max_length=256, null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='site_holiday_attachments', blank=True)
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL,
                             related_name="site_holidays")

    def __str__(self):
        return str(self.site) + ": " + str(self.name) + ": " + str(self.date)

    def is_owner(self, user):
        return (self.site is not None) and (hasattr(self.site, 'is_owner') and self.site.is_owner(user))

    # noinspection PyMethodMayBeStatic
    def is_member(self, user):
        return False


class LeaveStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft'),
    IN_REVIEW = 'IN_REVIEW', _('In Review'),
    APPROVED = 'APPROVED', _('Approved'),
    CLOSED = 'CLOSED', _('Closed'),


class Leave(models.Model):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="leaves")
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date')
    summary = models.CharField(max_length=256, null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='leave_attachments', blank=True)
    status = models.CharField(max_length=9, choices=LeaveStatus.choices, default=LeaveStatus.DRAFT)

    def __str__(self):
        return str(self.engineer) + " from " + str(self.start_date) + " to " + str(self.end_date) + " - " + str(
            self.status)

    def is_owner(self, user):
        return (self.engineer is not None) and (hasattr(self.engineer, 'is_owner') and self.engineer.is_owner(user))

    # noinspection PyMethodMayBeStatic
    def is_member(self, user):
        return False


class EngineerOrgGroupParticipationHistory(OrgModel):
    class Meta:
        verbose_name_plural = "engineer org-group participation history"

    date = models.DateField()
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="org_group_participation_history")
    expected_capacity = models.FloatField(default=1.0, verbose_name='expected capacity')
    capacity = models.FloatField(default=1.0)

    def __str__(self):
        return "On " + str(self.date) + ", " + str(self.engineer) + " participated in " + str(
            self.org_group) + " with capacity " + str(
            self.capacity)


class Epic(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='epic_attachments', blank=True)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='epics')

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Feature(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='feature_attachments', blank=True)

    epic = models.ForeignKey(Epic, null=True, on_delete=models.SET_NULL, related_name='features')

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Sprint(OrgModel):
    number = models.IntegerField()
    release = models.ForeignKey(Release, null=True, blank=True, on_delete=models.SET_NULL, related_name='sprints')
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date')

    def __str__(self):
        return str(self.release) + ": " + str(self.number)


class Story(OrgModel):
    class Meta:
        verbose_name_plural = "stories"

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='story_attachments', blank=True)
    rank = models.IntegerField()
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True)
    feature = models.ForeignKey(Feature, null=True, on_delete=models.SET_NULL, related_name='stories')

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class ReviewStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft'),
    IN_PROGRESS = 'IN_PROGRESS', _('In progress'),
    IN_REVIEW = 'IN_REVIEW', _('In Review'),
    APPROVED = 'APPROVED', _('Approved'),


class UseCaseCategory(OrgModel):
    class Meta:
        verbose_name_plural = "use case categories"

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class UseCase(OrgModel):
    category = models.ForeignKey(UseCaseCategory, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # pre_conditions = models.ManyToManyField(UseCasePreCondition, related_name="pre_condition_use_cases", blank=True)
    # events = models.ManyToManyField(UseCaseStep, related_name="event_use_cases", blank=True)
    # post_conditions = models.ManyToManyField(UseCasePostCondition, related_name="post_condition_use_cases",
    # blank=True)

    status = models.CharField(max_length=11, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    weight = models.FloatField(default=1)
    consumer_score = models.FloatField(default=0, verbose_name='consumer score')
    serviceability_score = models.FloatField(default=0, verbose_name='serviceability score')
    test_confidence = models.FloatField(default=0, verbose_name='test confidence')
    development_confidence = models.FloatField(default=0, verbose_name='development confidence')

    attachments = models.ManyToManyField(Attachment, related_name='use_case_attachments', blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)

    def get_score(self):
        return (self.consumer_score + self.serviceability_score + self.test_confidence + self.development_confidence) \
            / 4


class Requirement(OrgModel):
    use_cases = models.ManyToManyField(UseCase, related_name='requirements', blank=True)

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Tag(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Defect(OrgModel):
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    external_id = models.CharField(max_length=50, blank=True)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='defects')
    attachments = models.ManyToManyField(Attachment, related_name='defect_attachments', blank=True)


class Run(OrgModel):
    build = models.CharField(max_length=256)
    name = models.CharField(max_length=256, unique=True)
    time = models.DateTimeField(auto_now_add=True)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='runs')

    def __str__(self):
        return str(self.build) + ": " + str(self.name)


class ExecutionRecordStatus(models.TextChoices):
    PENDING = 'PENDING', _('Pending execution'),
    PASS = 'PASS', _('Passed'),
    FAILED = 'FAILED', _('Failed'),


class ExecutionRecord(OrgModel):
    run = models.ForeignKey(Run, null=True, on_delete=models.SET_NULL, related_name='execution_records')
    time = models.DateTimeField(auto_now_add=True)

    # use_case = models.ForeignKey(UseCase, on_delete=models.SET_NULL, null=True, related_name='execution_records')
    # testcase = models.ForeignKey(TestCase, null=True, on_delete=models.SET_NULL, related_name='execution_records')

    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=8, choices=ExecutionRecordStatus.choices,
                              default=ExecutionRecordStatus.PENDING)

    acceptance_test = models.BooleanField(default=False, verbose_name='is acceptance test')
    automated = models.BooleanField(default=False, verbose_name='is automated')

    # defects = models.CharField(max_length=200)
    defects = models.ManyToManyField(Defect, related_name='execution_records', blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


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
    # defects = models.CharField(max_length=200)
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
    attachments = models.ManyToManyField(Attachment, related_name='environment_attachments', blank=True)
    current_release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='environments',
                                        verbose_name='currently release')

    def __str__(self):
        return str(self.name) + ": " + str(self.type)


class Topic(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    parent_topic = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="sub_topics", verbose_name='parent topic')

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class TopicEngineerStatus(models.TextChoices):
    ASSIGNED = 'ASSIGNED', _('Assigned'),
    IN_PROGRESS = 'IN_PROGRESS', _('In Progress'),
    COMPLETED = 'COMPLETED', _('Completed'),


class TopicEngineerAssignment(OrgModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="engineer_ratings")
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="topic_ratings")
    status = models.CharField(max_length=11, choices=TopicEngineerStatus.choices, default=TopicEngineerStatus.ASSIGNED)
    rating = models.FloatField(default=0)
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date')

    def __str__(self):
        return str(self.topic.name) + ": " + str(self.engineer.name) + ": " + str(self.status)


class Feedback(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='feedbacks')

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)

# class TestStep:
#     def __init__(self):
#         self.step = None
#         self.testData = None  # {}
#         self.testDataSet = None  # {}
#         self.variableTestDataRules = None  # {}
#         self.node = None
#         self.numberOfThreads = 1
#         self.maxRetries = 0
#         self.steps = None
#         self.runStepsInParallel = False
#         self.condition = None
#
#
# class TestScenario:
#     def __init__(self):
#         self.name = None
#         self.description = None
#         self.probability = 1.0
#         self.setupSteps = None  # {}
#         self.chaosConfiguration = None
#         self.executionSteps = None  # {}
#         self.tearDownSteps = None  # {}
#         self.testDataSet = None  # {}
#
#
# class TestFeature:
#     def __init__(self):
#         self.name = None
#         self.description = None
#         self.testJobs = None
#         self.setupSteps = None  # {}
#         self.scenarioSetupSteps = None  # {}
#         self.testScenarios = None  # {}
#         self.scenarioTearDownSteps = None  # {}
#         self.tearDownSteps = None  # {}
#         self.testDataSet = None  # {}


# class StringStep(OrgModel):
#     summary = models.CharField(max_length=1024, unique=True)
#     description = models.TextField( null=True, blank=True)
#
#     def __str__(self):
#         return str(self.summary)


#
# class UseCasePreCondition(StringStep):
#     pass
#
#
# class UseCaseStep(StringStep):
#     actor = models.CharField(max_length=256, null=True, blank=True)
#     interface = models.CharField(max_length=256, null=True, blank=True)
#     action = models.CharField(max_length=256, null=True, blank=True)
#
#
# class UseCasePostCondition(StringStep):
#     pass
#
#
# class TestCasePreCondition(StringStep):
#     pass
#
#
# class TestCaseStep(StringStep):
#     pass
#
#
# class TestCasePostCondition(StringStep):
#     pass
