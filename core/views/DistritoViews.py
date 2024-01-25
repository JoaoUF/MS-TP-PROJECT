from core.serializers import DistritoSerializer
from core.models import Distrito
from rest_framework import mixins
from rest_framework import generics


class DistritoList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data['usuarioAdicion'] = request.data.pop('usuario')
        return self.create(request, *args, **kwargs)


class DistritoDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        request.data['usuarioModificacion'] = request.data.pop('usuario')
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)