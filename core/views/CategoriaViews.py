from core.serializers import CategoriaSerializer
from core.models import Categoria
from rest_framework import mixins
from rest_framework import generics


class CategoriaList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data['usuarioAdicion'] = request.data.pop('usuario')
        return self.create(request, *args, **kwargs)


class CategoriaDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        request.data['usuarioModificacion'] = request.data.pop('usuario')
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
