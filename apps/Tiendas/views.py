from rest_framework import generics
from apps.Tiendas.models import Tienda
from apps.Celulares.models import Celular
from apps.Tiendas.serializers import TiendaSerializer, CelularSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class TiendaListView(APIView):
   def get(self, request):
      tiendas = Tienda.objects.all()
      serializer = TiendaSerializer(tiendas, many=True)
      return Response(serializer.data)
   
class CelularesPorTiendaView(APIView):
   def get(self, request, id_tienda):
      celulares = Celular.objects.filter(tienda=id_tienda).exclude(estado_venta=1)
      serializer = CelularSerializer(celulares, many=True)
      return Response(serializer.data)