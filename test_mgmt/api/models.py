from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from api import ipte_util
from test_mgmt import settings


class Attachment(models.Model):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to=settings.MEDIA_BASE_NAME, blank=False, null=False)

    def __str__(self):
        return str(self.file.name)


class OrgGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    auth_group = models.OneToOneField(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name="org_group")
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    parent_org_group = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name="sub_org_groups")
    leader = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="lead_org_groups")
    attachments = models.ManyToManyField(Attachment, related_name='org_group_attachments', blank=True)

    def __str__(self):
        return str(self.name)


class Engineer(models.Model):
    employee_id = models.CharField(max_length=20, null=True, unique=True)
    auth_user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="engineer")
    role = models.CharField(max_length=100, null=True, blank=True, )
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, related_name="engineers", blank=True, null=True)
    attachments = models.ManyToManyField(Attachment, related_name='engineer_attachments', blank=True)

    def __str__(self):
        return str(self.employee_id) + ": " + str(self.auth_user)


class Release(models.Model):
    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name="releases")

    def __str__(self):
        return str(self.name)


class EngineerOrgGroupParticipation(models.Model):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="org_group_participation")
    org_group = models.ForeignKey(OrgGroup, on_delete=models.CASCADE, related_name="engineer_participation")
    role = models.CharField(max_length=100, null=True, blank=True, )
    capacity = models.FloatField(default=1.0)

    def __str__(self):
        return str(self.engineer) + ": " + str(self.org_group)


class SiteHoliday(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    summary = models.CharField(max_length=100, null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='site_holiday_attachments', blank=True)
    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="site_holidays")

    def __str__(self):
        return str(self.date) + ": " + str(self.name)


class Leave(models.Model):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="leaves")
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.CharField(max_length=100, null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='leave_attachments', blank=True)

    def __str__(self):
        return str(self.engineer) + ": " + str(self.start_date) + "-" + str(self.end_date) + str(self.summary)


class Epic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='epic_attachments', blank=True)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='epics')

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name="epics")

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='feature_attachments', blank=True)

    epic = models.ForeignKey(Epic, null=True, on_delete=models.SET_NULL, related_name='features')

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name="features")

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Sprint(models.Model):
    number = models.IntegerField()
    release = models.ForeignKey(Release, null=True, blank=True, on_delete=models.SET_NULL, related_name='sprints')
    start_date = models.DateField()
    end_date = models.DateField()

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name="sprints")

    def __str__(self):
        return str(self.release) + ": " + str(self.number)


class Story(models.Model):
    class Meta:
        verbose_name_plural = "stories"

    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='story_attachments', blank=True)
    rank = models.IntegerField()
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True)
    feature = models.ForeignKey(Feature, null=True, on_delete=models.SET_NULL, related_name='stories')

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name="stories")

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class ReviewStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft'),
    IN_REVIEW = 'IN_REVIEW', _('In Review'),
    APPROVED = 'APPROVED', _('Approved'),


class UseCaseCategory(models.Model):
    class Meta:
        verbose_name_plural = "use case categories"

    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="use_case_categories")

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class UseCase(models.Model):
    category = models.ForeignKey(UseCaseCategory, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)

    # pre_conditions = models.ManyToManyField(UseCasePreCondition, related_name="pre_condition_use_cases", blank=True)
    # events = models.ManyToManyField(UseCaseStep, related_name="event_use_cases", blank=True)
    # post_conditions = models.ManyToManyField(UseCasePostCondition, related_name="post_condition_use_cases",
    # blank=True)

    status = models.CharField(max_length=9, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    weight = models.FloatField(default=1)
    consumer_score = models.FloatField(default=0)
    serviceability_score = models.FloatField(default=0)
    test_confidence = models.FloatField(default=0)
    development_confidence = models.FloatField(default=0)

    attachments = models.ManyToManyField(Attachment, related_name='use_case_attachments', blank=True)

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name="use_cases")

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)

    def get_score(self):
        return (self.consumer_score + self.serviceability_score + self.test_confidence + self.development_confidence) \
               / 4


class Requirement(models.Model):
    use_cases = models.ManyToManyField(UseCase, related_name='requirements', blank=True)

    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="requirements")

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class TestCase(models.Model):
    use_case = models.ForeignKey(UseCase, on_delete=models.SET_NULL, null=True, related_name='testcases')
    requirements = models.ManyToManyField(Requirement, related_name='testcases', blank=True)

    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)

    attachments = models.ManyToManyField(Attachment, related_name='test_case_attachments', blank=True)

    status = models.CharField(max_length=9, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    # bdd_test_case = jsonfield.JSONField()
    # setup_steps = models.ManyToManyField(TestCasePreCondition, related_name="setup_steps_test_cases", blank=True)
    # steps = models.ManyToManyField(TestCaseStep, related_name="steps_test_cases", blank=True)
    # teardown_steps = models.ManyToManyField(TestCasePostCondition, related_name="teardown_steps_test_cases",
    # blank=True)

    acceptance_test = models.BooleanField(default=False)
    automated = models.BooleanField(default=False)

    # class TestExecutionStatus(models.TextChoices):
    #     PENDING = 'PENDING', _('Pending'),
    #     FAILED = 'FAILED', _('Failed'),
    #     PASSED = 'PASSED', _('Passed'),
    #
    # execution_status = models.CharField(max_length=8, choices=TestExecutionStatus.choices,
    #                                     default=TestExecutionStatus.PENDING)

    # defects = models.CharField(max_length=200, null=True, blank=True)

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name="testcases")

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Defect(models.Model):
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)
    external_id = models.CharField(max_length=50)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='defects')
    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name="defects")


class Run(models.Model):
    build = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='runs')
    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name="runs")

    def __str__(self):
        return str(self.build) + ": " + str(self.name)


class ExecutionRecordStatus(models.TextChoices):
    PENDING = 'PENDING', _('Pending execution'),
    PASS = 'PASS', _('Passed'),
    FAILED = 'FAILED', _('Failed'),


class ExecutionRecord(models.Model):
    run = models.ForeignKey(Run, null=True, on_delete=models.SET_NULL, related_name='execution_records')
    time = models.DateTimeField(auto_now_add=True)

    # use_case = models.ForeignKey(UseCase, on_delete=models.SET_NULL, null=True, related_name='execution_records')
    # testcase = models.ForeignKey(TestCase, null=True, on_delete=models.SET_NULL, related_name='execution_records')

    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)

    status = models.CharField(max_length=8, choices=ExecutionRecordStatus.choices,
                              default=ExecutionRecordStatus.PENDING)

    acceptance_test = models.BooleanField(default=False)
    automated = models.BooleanField(default=False)

    # defects = models.CharField(max_length=200)
    defects = models.ManyToManyField(Defect, related_name='execution_records', blank=True)

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="execution_records")

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class ReliabilityRunStatus(models.TextChoices):
    PENDING = 'PENDING', _('Pending execution'),
    IN_PROGRESS = 'IN_PROGRESS', _('In progress'),
    COMPLETED = 'COMPLETED', _('Completed'),


# noinspection PyTypeChecker
class ReliabilityRun(models.Model):
    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='reliability_runs')

    build = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)

    start_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    testName = models.CharField(max_length=200)
    testEnvironmentType = models.CharField(max_length=200)
    testEnvironmentName = models.CharField(max_length=200)

    status = models.CharField(max_length=11, choices=ReliabilityRunStatus.choices,
                              default=ReliabilityRunStatus.PENDING)

    totalIterationCount = models.IntegerField(null=True, blank=True)
    passedIterationCount = models.IntegerField(null=True, blank=True)
    incidentCount = models.IntegerField(null=True, blank=True)
    targetIPTE = models.FloatField(null=True, blank=True)
    ipte = models.FloatField(null=True, blank=True)
    # defects = models.CharField(max_length=200)
    incidents = models.ManyToManyField(Defect, related_name='reliability_runs', blank=True)

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="reliability_runs")

    def __str__(self):
        return str(self.name) + ": " + str(self.testName) + ": " + str(self.release.name) + ": " + str(self.build)

    def recalculate_ipti(self):
        self.ipte = -1.0
        if self.incidentCount and self.totalIterationCount:
            if self.totalIterationCount > 0:
                self.ipte = ipte_util.calculate_ipte(self.totalIterationCount, self.incidentCount)


class Environment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=20000, null=True, blank=True)
    purpose = models.CharField(max_length=1000, null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='environment_attachments', blank=True)
    current_release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='environments')

    org_group = models.ForeignKey(OrgGroup, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="environments")

    def __str__(self):
        return str(self.name) + ": " + str(self.type)

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


# class StringStep(models.Model):
#     summary = models.CharField(max_length=1000, unique=True)
#     description = models.CharField(max_length=10000, null=True, blank=True)
#
#     def __str__(self):
#         return str(self.summary)


#
# class UseCasePreCondition(StringStep):
#     pass
#
#
# class UseCaseStep(StringStep):
#     actor = models.CharField(max_length=100, null=True, blank=True)
#     interface = models.CharField(max_length=100, null=True, blank=True)
#     action = models.CharField(max_length=100, null=True, blank=True)
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
