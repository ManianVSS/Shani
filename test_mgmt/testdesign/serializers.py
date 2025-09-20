from api.models import org_model_base_fields
from api.serializers import ShaniModelSerializer
from .models import TestCase, Attachment, TestCaseCategory, Tag


class TestDesignAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class TestDesignTagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class TestCaseCategorySerializer(ShaniModelSerializer):
    class Meta:
        model = TestCaseCategory
        fields = org_model_base_fields + ['name', 'summary', 'description', 'weight', 'parent', 'tags', 'details_file',
                                          'attachments', ]


class TestCaseSerializer(ShaniModelSerializer):
    class Meta:
        model = TestCase
        fields = org_model_base_fields + ['name', 'summary', 'parent', 'status', 'type', 'tags', 'external_id',
                                          'specification', 'details_file', 'use_cases', 'attachments', ]


serializer_map = {
    Attachment: TestDesignAttachmentSerializer,
    Tag: TestDesignTagSerializer,
    TestCaseCategory: TestCaseCategorySerializer,
    TestCase: TestCaseSerializer,
}
