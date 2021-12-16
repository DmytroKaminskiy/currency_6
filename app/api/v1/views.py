from rest_framework import viewsets

from .pagination import RatePagination
from .serializer import RateSerializer
from .filters import RateFilter
from currency.models import Rate

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


# class SourceViewSet:
#     throttle_classes = [AnonCurrencyThrottle]
