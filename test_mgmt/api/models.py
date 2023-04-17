from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.translation import gettext_lazy as _

from test_mgmt import settings


# noinspection PyMethodMayBeStatic
class BaseModel(models.Model):
    class Meta:
        abstract = True

    published = models.BooleanField(default=False, verbose_name='is published content')

    def __str__(self):
        if hasattr(self, 'name'):
            string_value = str(self.name)
            if hasattr(self, 'summary'):
                if self.summary is not None:
                    string_value = string_value + ":" + str(self.summary)
        else:
            string_value = str(self.id)
        return string_value

    def is_guest(self, user):
        return user is not None

    def is_member(self, user):
        return user is not None

    def is_owner(self, user):
        return user is not None

    def can_read(self, user):
        return self.is_owner(user) or self.is_member(user) or (self.published and self.is_guest(user))

    def can_modify(self, user):
        return self.is_owner(user) or self.is_member(user)

    def can_delete(self, user):
        return self.is_owner(user)


# noinspection PyUnresolvedReferences
class OrgGroup(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    auth_group = models.OneToOneField(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name="org_group",
                                      verbose_name='authorization group')
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    org_group = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="sub_org_groups", verbose_name='parent organization group')
    leaders = models.ManyToManyField(User, blank=True, related_name="org_group_leaders")
    members = models.ManyToManyField(User, blank=True, related_name="org_group_members")
    guests = models.ManyToManyField(User, blank=True, related_name="org_group_guests")

    def is_owner(self, user):
        return ((self.leaders is not None) and (user in self.leaders.all())) or (
                (self.org_group is not None) and self.org_group.is_owner(user))

    def is_member(self, user):
        return ((self.members is not None) and (user in self.members.all())) or (
                (self.org_group is not None) and self.org_group.is_member(user))

    def is_guest(self, user):
        return ((self.guests is not None) and (user in self.guests.all())) or (
                (self.org_group is not None) and self.org_group.is_guest(user))


# noinspection PyUnresolvedReferences
class OrgModel(BaseModel):
    class Meta:
        abstract = True

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group')

    def can_read(self, user):
        return (self.org_group is None) or self.org_group.is_owner(user) or self.org_group.is_member(user) or (
                self.published and self.org_group.is_guest(user))

    def can_modify(self, user):
        return (self.org_group is None) or self.org_group.is_owner(user) or self.org_group.is_member(user)

    def can_delete(self, user):
        return (self.org_group is None) or self.org_group.is_owner(user)

    def is_owner(self, user):
        return (self.org_group is None) or self.org_group.is_owner(user)

    def is_member(self, user):
        return (self.org_group is None) or self.org_group.is_member(user)

    def is_guest(self, user):
        return (self.org_group is None) or self.org_group.is_guest(user)


class ReviewStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft'),
    IN_PROGRESS = 'IN_PROGRESS', _('In progress'),
    IN_REVIEW = 'IN_REVIEW', _('In Review'),
    APPROVED = 'APPROVED', _('Approved'),


class Attachment(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='api_attachments')
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to=settings.MEDIA_BASE_NAME, blank=False, null=False)
