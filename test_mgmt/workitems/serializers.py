from rest_framework import serializers

from .models import Attachment, Tag, Release, Story, Sprint, Feature, Epic, Feedback


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', ]


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'name', 'summary', 'description', 'org_group', ]


class EpicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epic
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'release', 'org_group', ]


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'epic', 'org_group', ]


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id', 'number', 'release', 'start_date', 'end_date', 'org_group', ]


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'rank', 'sprint', 'feature',
                  'org_group', ]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'summary', 'description', 'time', 'release', 'org_group', ]
