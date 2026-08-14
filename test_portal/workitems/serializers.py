from api.models import org_model_base_fields
from api.serializers import ShaniModelSerializer
from .models import Attachment, Tag, ProgramIncrement, Story, Sprint, Feature, Epic, Feedback


class WorkitemsAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class WorkitemsTagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ProgramIncrementSerializer(ShaniModelSerializer):
    class Meta:
        model = ProgramIncrement
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class EpicSerializer(ShaniModelSerializer):
    class Meta:
        model = Epic
        fields = org_model_base_fields + ['name', 'summary', 'description', 'weight', 'attachments', 'pi', ]


class WorkitemsFeatureSerializer(ShaniModelSerializer):
    class Meta:
        model = Feature
        fields = org_model_base_fields + ['name', 'summary', 'description', 'weight', 'attachments', 'epic', ]


class SprintSerializer(ShaniModelSerializer):
    class Meta:
        model = Sprint
        fields = org_model_base_fields + ['name', 'pi', 'start_date', 'end_date', ]


class StorySerializer(ShaniModelSerializer):
    class Meta:
        model = Story
        fields = org_model_base_fields + ['name', 'summary', 'description', 'weight', 'attachments', 'rank', 'sprint',
                                          'feature', ]


class FeedbackSerializer(ShaniModelSerializer):
    class Meta:
        model = Feedback
        fields = org_model_base_fields + ['name', 'summary', 'description', 'time', 'pi', ]


serializer_map = {
    Attachment: WorkitemsAttachmentSerializer,
    Tag: WorkitemsTagSerializer,
    ProgramIncrement: ProgramIncrementSerializer,
    Epic: EpicSerializer,
    Feature: WorkitemsFeatureSerializer,
    Sprint: SprintSerializer,
    Story: StorySerializer,
    Feedback: FeedbackSerializer,
}
