from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .pagination import RatePagination
from .serializer import RateSerializer
from .filters import RateFilter
from currency.models import Rate, Source
from currency import model_choices as mch, consts

from django.core.cache import cache
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from rest_framework.renderers import JSONRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_xml.renderers import XMLRenderer

from .throttles import AnonCurrencyThrottle


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer  # json.loads, json.dumps
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'sale', 'buy']
    throttle_classes = [AnonCurrencyThrottle]
    # permission_classes = (AllowAny, )
    # renderer_classes = (JSONRenderer, YAMLRenderer, XMLRenderer)
    # http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']

    def perform_create(self, serializer):
        super().perform_create(serializer)
        # send email


class LatestRatesView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        latest_rates = cache.get(consts.LATEST_RATE_KEY)
        if latest_rates is not None:
            return Response({'rates': latest_rates})

        latest_rates = []
        for source_obj in Source.objects.all():
            for currency_type in mch.RateTypeChoices:
                latest_rate = Rate.objects\
                    .filter(type=currency_type, source=source_obj)\
                    .order_by('-created')\
                    .first()
                if latest_rate:
                    latest_rates.append(RateSerializer(latest_rate).data)

        cache.set(consts.LATEST_RATE_KEY, latest_rates, 60 * 60 * 24 * 7)
        return Response({'rates': latest_rates})

# class SourceViewSet:
#     throttle_classes = [AnonCurrencyThrottle]
