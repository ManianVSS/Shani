from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.translation import gettext_lazy as _

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

