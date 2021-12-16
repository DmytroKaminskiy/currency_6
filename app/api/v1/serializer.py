from rest_framework import serializers

from currency.models import Rate


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'sale',
            'buy',
            'created',
            'source',
            'type',
        )

    def create(self, validated_data):
        instance = super().create(validated_data)
        # send email
        return instance
