Habilitar configuração de cabeçalhos do Django CORS (Cross Origin Resource Sharing)

Instale o módulo usando o PIP

pip install django-cors-headers

No arquivo [OME_HOME] /lib/python/omeroweb/settings.py, adicione o módulo aos aplicativos instalados

INSTALLED_APPS = (
    ...
    'pipeline',
    'corsheaders'
)

e adicione o middleware aos disponíveis

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
)

Note que CorsMiddlewareprecisa vir antes do Django CommonMiddlewarese você estiver usando a USE_ETAGS = Trueconfiguração do Django , caso contrário os cabeçalhos do CORS serão perdidos das 304 respostas não modificadas, causando erros em alguns navegadores.

Módulo pode ser configurado no mesmo arquivo, adicionar parâmetros de configuração antes do bloco

# Load server list and freeze
from connector import Server

def load_server_list():
    for s in SERVER_LIST:  # from CUSTOM_SETTINGS_MAPPINGS  # noqa
        server = (len(s) > 2) and unicode(s[2]) or None
        Server(host=unicode(s[0]), port=int(s[1]), server=server)
    Server.freeze()
load_server_list()
Se, por exemplo, você quiser permitir que apenas um domínio possa se comunicar com o back-end, sua configuração será

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    '<YOUR_DOMAIN>[:PORT]',
)
Evitando o "erro de muitos arquivos abertos"
O uso intensivo da biblioteca aleatória pelo plug-in de cabeçalhos CORS pode produzir o erro

OSError: [Errno 24] Too many open files: '/dev/urandom'
Para resolver este problema é necessário atualizar o arquivo /etc/security/limit.conf para garantir um valor de 65535 arquivos abertos como este exemplo

#<domain>                      <type>  <item>         <value>
#
<omero_srv_user>               soft     nofile          65535
<omero_srv_user>               hard     nofile          65535
onde <omero_srv_user> é o usuário executando o OMERO em seu servidor.

O servidor deve ser reiniciado para tornar essa alteração efetiva.