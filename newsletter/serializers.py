from rest_framework.serializers import ModelSerializer

from newsletter.models import Subscription, Newsletter


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ["id", "title", "slug"]


class SubscriptionSerializerBase(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["user", "newsletter", "subscribed"]
        read_only_fields = ["user"]


class SubscriptionSerializer(SubscriptionSerializerBase):
    newsletter = NewsletterSerializer()
