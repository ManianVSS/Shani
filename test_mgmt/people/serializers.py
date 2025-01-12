from api.serializers import ShaniModelSerializer
from .models import Engineer, SiteHoliday, Leave, EngineerOrgGroupParticipation, Topic, \
    TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Attachment, Credit, Scale, Reason, \
    EngineerSkills


class AttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class EngineerSerializer(ShaniModelSerializer):
    class Meta:
        model = Engineer
        fields = ['id', 'employee_id', 'name', 'auth_user', 'role', 'org_group', 'created_at', 'updated_at',
                  'published', 'site', 'points', 'attachments', ]


class EngineerOrgGroupParticipationSerializer(ShaniModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipation
        fields = ['id', 'engineer', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', 'role',
                  'capacity', ]


class SiteHolidaySerializer(ShaniModelSerializer):
    class Meta:
        model = SiteHoliday
        fields = ['id', 'name', 'date', 'summary', 'attachments', 'site', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class LeaveSerializer(ShaniModelSerializer):
    class Meta:
        model = Leave
        fields = ['id', 'engineer', 'start_date', 'end_date', 'summary', 'attachments', 'status', 'created_at',
                  'updated_at', 'published', ]


class EngineerOrgGroupParticipationHistorySerializer(ShaniModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipationHistory
        fields = ['id', 'date', 'engineer', 'org_group', 'created_at', 'updated_at', 'published', 'is_public',
                  'expected_capacity',
                  'capacity', ]


class TopicSerializer(ShaniModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'summary', 'description', 'parent_topic', 'org_group', 'created_at', 'updated_at',
                  'published', ]


class TopicEngineerAssignmentSerializer(ShaniModelSerializer):
    class Meta:
        model = TopicEngineerAssignment
        fields = ['id', 'topic', 'engineer', 'status', 'rating', 'start_date', 'end_date', 'org_group', 'created_at',
                  'updated_at', 'published', ]


class ScaleSerializer(ShaniModelSerializer):
    class Meta:
        model = Scale
        fields = ['id', 'name', 'summary', 'description', ]


class ReasonSerializer(ShaniModelSerializer):
    class Meta:
        model = Reason
        fields = ['id', 'name', 'summary', 'description', 'weight', ]


class CreditSerializer(ShaniModelSerializer):
    class Meta:
        model = Credit
        fields = ['id', 'time', 'credited_user', 'credits', 'scale', 'reason', 'description', 'creditor', 'org_group',
                  'created_at', 'updated_at', 'published', 'is_public', ]


class EngineerSkillsSerializer(ShaniModelSerializer):
    class Meta:
        model = EngineerSkills
        fields = ['id', 'engineer', 'skill', 'experience', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


serializer_map = {
    Attachment: AttachmentSerializer,
    Engineer: EngineerSerializer,
    EngineerOrgGroupParticipation: EngineerOrgGroupParticipationSerializer,
    SiteHoliday: SiteHolidaySerializer,
    Leave: LeaveSerializer,
    EngineerOrgGroupParticipationHistory: EngineerOrgGroupParticipationHistorySerializer,
    Topic: TopicSerializer,
    TopicEngineerAssignment: TopicEngineerAssignmentSerializer,
    Scale: ScaleSerializer,
    Reason: ReasonSerializer,
    Credit: CreditSerializer,
    EngineerSkills: EngineerSkillsSerializer,
}
