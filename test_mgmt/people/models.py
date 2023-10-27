from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import OrgModel, OrgGroup, BaseModel
from api.storage import CustomFileSystemStorage


class Attachment(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='people_attachments')
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='execution', blank=False, null=False)


class Site(OrgModel):
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='site_attachments', blank=True)


class Engineer(OrgModel):
    employee_id = models.CharField(max_length=20, null=True, unique=True, verbose_name='employee id')
    name = models.CharField(max_length=256, default='<unnamed>')
    auth_user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="engineer",
                                     verbose_name='authorization user')
    role = models.CharField(max_length=256, null=True, blank=True, )
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL,
                             related_name="engineers")
    points = models.FloatField(default=0)
    attachments = models.ManyToManyField(Attachment, related_name='engineer_attachments', blank=True)

    def __str__(self):
        return str(self.auth_user)

    def is_guest(self, user):
        return user == self.auth_user


class EngineerOrgGroupParticipation(OrgModel):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="org_group_participation")
    role = models.CharField(max_length=256, null=True, blank=True, )
    capacity = models.FloatField(default=1.0)

    def __str__(self):
        return str(self.engineer) + " participates in " + str(self.org_group) + " with capacity " + str(
            self.capacity)


class SiteHoliday(BaseModel):
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

    def is_guest(self, user):
        return False

    def can_read(self, user):
        return self.is_owner(user)


class LeaveStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft'),
    IN_REVIEW = 'IN_REVIEW', _('In Review'),
    APPROVED = 'APPROVED', _('Approved'),
    CLOSED = 'CLOSED', _('Closed'),


class Leave(BaseModel):
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

    def is_guest(self, user):
        return False

    # noinspection PyUnresolvedReferences
    def can_read(self, user):
        return self.is_owner(user) or (user == self.engineer.auth_user)


class EngineerOrgGroupParticipationHistory(OrgModel):
    class Meta:
        verbose_name_plural = "engineer org-group participation history"

    date = models.DateField()
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="org_group_participation_history")
    expected_capacity = models.FloatField(default=1.0, verbose_name='expected capacity')
    capacity = models.FloatField(default=1.0)

    def __str__(self):
        return "On " + str(self.date) + ", " + str(self.engineer) + " participated in " + str(
            self.org_group) + " with capacity " + str(self.capacity)


class Topic(OrgModel):
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    parent_topic = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="sub_topics", verbose_name='parent topic')


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

    def is_owner(self, user):
        return (self.engineer is not None) and (hasattr(self.engineer, 'is_owner') and self.engineer.is_owner(user))

    # noinspection PyMethodMayBeStatic
    def is_member(self, user):
        return False

    def is_guest(self, user):
        return False

    # noinspection PyUnresolvedReferences
    def can_read(self, user):
        return self.is_owner(user) or (user == self.engineer.auth_user)


class Scale(OrgModel):
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Reason(OrgModel):
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)


class Credit(OrgModel):
    time = models.DateTimeField(auto_now=True, verbose_name="last modification time")
    credited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="credits_received",
                                      verbose_name="credited individual")
    credits = models.FloatField(default=0)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE, related_name="credits")
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, related_name="credits")
    description = models.TextField(default="<reason for credits>")
    creditor = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="credits_given")

    def can_modify(self, user):
        return self.is_owner(user)

    def is_owner(self, user):
        return (self.credited_user != user) and (
                (self.creditor == user) or (hasattr(self.org_group, 'is_owner') and self.org_group.is_owner(user)))

    def is_member(self, user):
        return (self.credited_user != user) and ((self.creditor == user) or (
                hasattr(self.org_group, 'is_member') and self.org_group.is_member(user)))

    def is_guest(self, user):
        return self.credited_user == user or (hasattr(self.org_group, 'is_guest') and self.org_group.is_guest(user))

    # noinspection PyUnresolvedReferences
    def __str__(self):
        return str(self.credited_user.username) + ": " + str(self.credits)


class EngineerSkills(OrgModel):
    class Meta:
        verbose_name_plural = "engineer skills"

    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="skills")
    skill = models.CharField(max_length=256, null=True, blank=True, )
    experience = models.FloatField(default=0)

    # def __str__(self):
    #     return str(self.engineer) + " has the skill " + str(self.skill) + " with experience " + str(self.capacity)
