from core.serializers import EntradaSerializer
from core.models import Entrada
from rest_framework import mixins
from rest_framework import generics


class EntradaList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data['usuarioAdicion'] = request.data.pop('usuario')[0]
        return self.create(request, *args, **kwargs)


class EntradaDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        request.data['usuarioModificacion'] = request.data.pop('usuario')[0]
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
