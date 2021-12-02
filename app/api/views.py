from rest_framework import viewsets

from api.serializer import RateSerializer
from currency.models import Rate

from rest_framework.renderers import JSONRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_xml.renderers import XMLRenderer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer  # json.loads, json.dumps
    # renderer_classes = (JSONRenderer, YAMLRenderer, XMLRenderer)
    # http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']
