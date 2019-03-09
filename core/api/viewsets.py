from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    # queryset = PontoTuristico.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.all()

    # List é para o listar todos os itens do endpoint
    # Verbo html GET em todos os registros
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    # Verbo html POST
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # Sempre editar o método DELETAR nas APIs para controlar permissões, logs e tipo de delete(físico ou lógico)
    # Verbo html DELETE
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # Retrieve é para o buscar apenas um item do endpoint
    # Verbo html GET em um registro
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    # Atualiza todos os atributos do registro
    # Verbo html PUT
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # Atualiza parte dos atributos do registro
    # Verbo html PATCH
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # Definir onde o endpoint será disparado (methods)
    # Para recuperar a PK (detail=True) para o endpoint (detail=False)
    # http://127.0.0.1:8000/pontosturisticos/1/denunciar
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    # http://127.0.0.1:8000/pontosturisticos/teste
    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass