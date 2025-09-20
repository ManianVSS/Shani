from api.models import base_model_base_fields, org_model_base_fields
from api.serializers import ShaniModelSerializer
from .models import Attachment, Tag, Step, Properties, MockAPI, ApplicationUnderTest, ApplicationPage, Element


class AutomationAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class AutomationTagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class StepSerializer(ShaniModelSerializer):
    class Meta:
        model = Step
        fields = org_model_base_fields + ['feature', 'name', 'summary', 'description', 'eta', 'tags', 'status',
                                          'details_file', 'attachments', ]


class PropertiesSerializer(ShaniModelSerializer):
    class Meta:
        model = Properties
        fields = org_model_base_fields + ['name', 'details', ]


class MockAPISerializer(ShaniModelSerializer):
    class Meta:
        model = MockAPI
        fields = org_model_base_fields + ['name', 'summary', 'status', 'content_type', 'body', 'http_method', ]


class ApplicationUnderTestSerializer(ShaniModelSerializer):
    class Meta:
        model = ApplicationUnderTest
        fields = org_model_base_fields + ['name', 'details', 'attachments', ]


class ApplicationPageSerializer(ShaniModelSerializer):
    class Meta:
        model = ApplicationPage
        fields = org_model_base_fields + ['application', 'name', 'details', 'attachments', ]


class ElementSerializer(ShaniModelSerializer):
    class Meta:
        model = Element
        fields = org_model_base_fields + ['page', 'name', 'containing_element', 'element_type', 'details',
                                          'locator_type', 'locator_value', 'locator_file', 'attachments', ]


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
