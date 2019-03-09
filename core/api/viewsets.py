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
    # def list(self, request, *args, **kwargs):
    #    return Response({'Teste': 123})

    # Verbo html POST
    # def create(self, request, *args, **kwargs):
    #     return Response({'Hello': requeste.data['nome']})

    # Sempre editar o método DELETAR nas APIs para controlar permissões, logs e tipo de delete(físico ou lógico)
    # Verbo html DELETE
    def destroy(self, request, *args, **kwargs):
        pass

    # Retrieve é para o buscar apenas um item do endpoint
    # Verbo html GET em um registro
    def retrieve(self, request, *args, **kwargs):
        pass

    # Atualiza todos os atributos do registro
    # Verbo html PUT
    def update(self, request, *args, **kwargs):
        pass

    # Atualiza parte dos atributos do registro
    # Verbo html PATCH
    def partial_update(self, request, *args, **kwargs):
        pass
