from api.serializers import ShaniModelSerializer
from .models import Attachment, Tag, Step, Properties, MockAPI, ApplicationUnderTest, ApplicationPage, Element


class AutomationAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class AutomationTagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class StepSerializer(ShaniModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'feature', 'name', 'summary', 'description', 'eta', 'tags', 'status', 'details_file',
                  'attachments', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class PropertiesSerializer(ShaniModelSerializer):
    class Meta:
        model = Properties
        fields = ['id', 'name', 'details', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class MockAPISerializer(ShaniModelSerializer):
    class Meta:
        model = MockAPI
        fields = ['id', 'name', 'summary', 'status', 'content_type', 'body', 'http_method', 'org_group', 'created_at',
                  'updated_at', 'published', 'is_public', ]


class ApplicationUnderTestSerializer(ShaniModelSerializer):
    class Meta:
        model = ApplicationUnderTest
        fields = ['id', 'name', 'details', 'attachments', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ApplicationPageSerializer(ShaniModelSerializer):
    class Meta:
        model = ApplicationPage
        fields = ['id', 'application', 'name', 'details', 'attachments', 'org_group', 'created_at', 'updated_at',
                  'published', 'is_public', ]


class ElementSerializer(ShaniModelSerializer):
    class Meta:
        model = Element
        fields = ['id', 'page', 'name', 'containing_element', 'element_type', 'details', 'locator_type',
                  'locator_value', 'locator_file', 'attachments', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


serializer_map = {
    Attachment: AutomationAttachmentSerializer,
    Tag: AutomationTagSerializer,
    Step: StepSerializer,
    Properties: PropertiesSerializer,
    MockAPI: MockAPISerializer,
    ApplicationUnderTest: ApplicationUnderTestSerializer,
    ApplicationPage: ApplicationPageSerializer,
    Element: ElementSerializer,
}
