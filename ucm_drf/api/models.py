from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from ucm_drf import settings


# import jsonfield


class Attachment(models.Model):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to=settings.MEDIA_BASE_NAME, blank=False, null=False)

    def __str__(self):
        return str(self.file.name)


class Release(models.Model):
    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)


class Epic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    weight = models.FloatField(null=True)
    attachments = models.ManyToManyField(Attachment, related_name='epic_attachments', blank=True)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='epics')

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    weight = models.FloatField(null=True)
    attachments = models.ManyToManyField(Attachment, related_name='feature_attachments', blank=True)

    epic = models.ForeignKey(Epic, null=True, on_delete=models.SET_NULL, related_name='features')

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Sprint(models.Model):
    number = models.IntegerField()
    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='sprints')
    start_date = models.DateField()
    end_date = models.DateField()


class Story(models.Model):
    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    weight = models.FloatField(null=True)
    attachments = models.ManyToManyField(Attachment, related_name='story_attachments', blank=True)
    rank = models.IntegerField()
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True)
    feature = models.ForeignKey(Feature, null=True, on_delete=models.SET_NULL, related_name='stories')

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


# class StringStep(models.Model):
#     summary = models.CharField(max_length=1000, unique=True)
#     description = models.CharField(max_length=10000, null=True)
#
#     def __str__(self):
#         return str(self.summary)


#
# class UseCasePreCondition(StringStep):
#     pass
#
#
# class UseCaseStep(StringStep):
#     actor = models.CharField(max_length=100, null=True)
#     interface = models.CharField(max_length=100, null=True)
#     action = models.CharField(max_length=100, null=True)
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


class ReviewStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft'),
    IN_REVIEW = 'IN_REVIEW', _('In Review'),
    APPROVED = 'APPROVED', _('Approved'),


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


class UseCase(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, null=True)

    # pre_conditions = models.ManyToManyField(UseCasePreCondition, related_name="pre_condition_use_cases", blank=True)
    # events = models.ManyToManyField(UseCaseStep, related_name="event_use_cases", blank=True)
    # post_conditions = models.ManyToManyField(UseCasePostCondition, related_name="post_condition_use_cases",
    # blank=True)

    status = models.CharField(max_length=9, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    weight = models.FloatField(null=True)
    consumer_score = models.FloatField(null=True)
    serviceability_score = models.FloatField(null=True)
    test_confidence = models.FloatField(null=True)
    development_confidence = models.FloatField(null=True)

    attachments = models.ManyToManyField(Attachment, related_name='use_case_attachments', blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)

    def get_score(self):
        return (self.consumer_score + self.serviceability_score + self.test_confidence + self.development_confidence) \
               / 4


class Requirement(models.Model):
    use_cases = models.ManyToManyField(UseCase, related_name='requirements', blank=True)

    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class TestCase(models.Model):
    use_case = models.ForeignKey(UseCase, on_delete=models.SET_NULL, null=True, related_name='testcases')
    requirements = models.ManyToManyField(Requirement, related_name='testcases', blank=True)

    name = models.CharField(max_length=100, unique=True)
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, null=True)

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

    # defects = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)


class Defect(models.Model):
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, null=True)
    external_id = models.CharField(max_length=50)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='defects')


class Run(models.Model):
    build = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(auto_now_add=True)

    release = models.ForeignKey(Release, null=True, on_delete=models.SET_NULL, related_name='runs')

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
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, null=True)

    status = models.CharField(max_length=8, choices=ExecutionRecordStatus.choices,
                              default=ExecutionRecordStatus.PENDING)

    acceptance_test = models.BooleanField(default=False)
    automated = models.BooleanField(default=False)

    # defects = models.CharField(max_length=200)
    defects = models.ManyToManyField(Defect, related_name='execution_records', blank=True)

    def __str__(self):
        return str(self.name) + ": " + str(self.summary)
