from core.serializers import TipoUsuarioSerializer
from core.models import TipoUsuario
from rest_framework import mixins
from rest_framework import generics


class TipoUsuarioList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data['usuarioAdicion'] = request.data.pop('usuario')
        return self.create(request, *args, **kwargs)


class TipoUsuarioDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        request.data['usuarioModificacion'] = request.data.pop('usuario')
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
