from api.models import base_model_base_fields, org_model_base_fields
from api.serializers import ShaniModelSerializer
from .models import Engineer, SiteHoliday, Leave, EngineerOrgGroupParticipation, Topic, \
    TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Attachment, Credit, Scale, Reason, \
    EngineerSkills


class PeopleAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class EngineerSerializer(ShaniModelSerializer):
    class Meta:
        model = Engineer
        fields = org_model_base_fields + ['employee_id', 'name', 'auth_user', 'role', 'site', 'points', 'attachments', ]


class EngineerOrgGroupParticipationSerializer(ShaniModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipation
        fields = org_model_base_fields + ['engineer', 'role', 'capacity', ]


class SiteHolidaySerializer(ShaniModelSerializer):
    class Meta:
        model = SiteHoliday
        fields = base_model_base_fields + ['name', 'date', 'summary', 'attachments', 'site', ]


class LeaveSerializer(ShaniModelSerializer):
    class Meta:
        model = Leave
        fields = base_model_base_fields + ['engineer', 'start_date', 'end_date', 'summary', 'attachments', 'status', ]


class EngineerOrgGroupParticipationHistorySerializer(ShaniModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipationHistory
        fields = org_model_base_fields + ['date', 'engineer', 'expected_capacity', 'capacity', ]


class TopicSerializer(ShaniModelSerializer):
    class Meta:
        model = Topic
        fields = org_model_base_fields + ['name', 'summary', 'description', 'parent_topic', ]


class TopicEngineerAssignmentSerializer(ShaniModelSerializer):
    class Meta:
        model = TopicEngineerAssignment
        fields = org_model_base_fields + ['topic', 'engineer', 'status', 'rating', 'start_date', 'end_date', ]


class ScaleSerializer(ShaniModelSerializer):
    class Meta:
        model = Scale
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ReasonSerializer(ShaniModelSerializer):
    class Meta:
        model = Reason
        fields = org_model_base_fields + ['name', 'summary', 'description', 'weight', ]


class CreditSerializer(ShaniModelSerializer):
    class Meta:
        model = Credit
        fields = org_model_base_fields + ['time', 'credited_user', 'credits', 'scale', 'reason', 'description',
                                          'creditor', ]


class EngineerSkillsSerializer(ShaniModelSerializer):
    class Meta:
        model = EngineerSkills
        fields = org_model_base_fields + ['engineer', 'skill', 'experience', ]


serializer_map = {
    Attachment: PeopleAttachmentSerializer,
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
