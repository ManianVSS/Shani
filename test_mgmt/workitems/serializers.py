from api.serializers import ShaniModelSerializer
from .models import Attachment, Tag, ProgramIncrement, Story, Sprint, Feature, Epic, Feedback


class AttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class TagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ProgramIncrementSerializer(ShaniModelSerializer):
    class Meta:
        model = ProgramIncrement
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class EpicSerializer(ShaniModelSerializer):
    class Meta:
        model = Epic
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'pi', 'org_group', 'created_at',
                  'updated_at', 'published', 'is_public', ]


class FeatureSerializer(ShaniModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'epic', 'org_group', 'created_at',
                  'updated_at', 'published', ]


class SprintSerializer(ShaniModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id', 'name', 'pi', 'start_date', 'end_date', 'org_group', 'created_at', 'updated_at',
                  'published', ]


class StorySerializer(ShaniModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'rank', 'sprint', 'feature',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class FeedbackSerializer(ShaniModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'summary', 'description', 'time', 'pi', 'org_group', 'created_at', 'updated_at',
                  'published', ]


serializer_map = {
    Attachment: AttachmentSerializer,
    Tag: TagSerializer,
    ProgramIncrement: ProgramIncrementSerializer,
    Epic: EpicSerializer,
    Feature: FeatureSerializer,
    Sprint: SprintSerializer,
    Story: StorySerializer,
    Feedback: FeedbackSerializer,
}
