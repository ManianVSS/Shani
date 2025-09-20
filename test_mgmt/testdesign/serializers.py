from api.serializers import ShaniModelSerializer
from .models import TestCase, Attachment, TestCaseCategory, Tag


class TestDesignAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class TestDesignTagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class TestCaseCategorySerializer(ShaniModelSerializer):
    class Meta:
        model = TestCaseCategory
        fields = ['id', 'name', 'summary', 'description', 'weight', 'parent', 'tags', 'details_file', 'attachments',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class TestCaseSerializer(ShaniModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'name', 'summary', 'parent', 'status', 'type', 'tags', 'external_id', 'specification',
                  'details_file', 'use_cases', 'attachments', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


serializer_map = {
    Attachment: TestDesignAttachmentSerializer,
    Tag: TestDesignTagSerializer,
    TestCaseCategory: TestCaseCategorySerializer,
    TestCase: TestCaseSerializer,
}
