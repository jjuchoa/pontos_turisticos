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

    # def list(self, request, *args, **kwargs):
    #    return Response({'Teste': 123})

    # def create(self, request, *args, **kwargs):
    #     return Response({'Hello': requeste.data['nome']})

    # Sempre editar o método DELETAR nas APIs para controlar permissões, logs e tipo de delete(físico ou lógico)
    def destroy(self, request, *args, **kwargs):
        pass
