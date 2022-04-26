# Versão 1

A primeira versão da plataforma utiliza os seguintes componentes: 

- [Orion Context Broker](https://github.com/telefonicaid/fiware-orion/)
- [IoT Agent JSON](https://github.com/telefonicaid/iotagent-json/blob/master/README.md)
- [MongoDB](https://www.mongodb.com/)
- [Django webserver](https://www.djangoproject.com/)

A comunicação entre os componentes é apresentado na figura abaixo. 

![Arquitetura da versão 1](./img/version1.png)

Para o funcionamento da plataforma é necessário utilizar o [Docker](https://www.docker.com/). Para maiores detalhes da instalação e configuração do Docker, consulte o [Manual do Docker](https://docs.docker.com/install/).

Uma vez instalado é possível montar todos os componentes utilizando o comando `docker compose up` no terminal do computador. Caso queria, também é possivel executar o comando `docker compose up -d` para que os componentes sejam iniciados mas que o log não seja apresentado no terminal. Para desmontar os componentes utilize o comando `docker compose down`. É possível conferir a situação de cada componente utilizando o comando `docker compose ps`. 

Quando todos os componentes estiverem rodando, é possível utilizar um cliente REST para fazer requisições HTTP para o IoT Agent, o Orion Context Broker e o servidor web. Utilize os seguintes comandos:

# Comandos para o Orion Context Broker. 

## Verificar informações sobre o Orion Context Broker. 

```bash
curl -X GET \
  'http://localhost:1026/version' \
  --header 'Accept: */*' \
```

A resposta deve ser algo parecido com: 

```json
{
  "orion": {
    "version": "3.6.0",
    "uptime": "0 d, 0 h, 2 m, 27 s",
    "git_hash": "973850279e63d58cb93dff751648af5ec6e05777",
    "compile_time": "Wed Mar 2 10:34:48 UTC 2022",
    "compiled_by": "root",
    "compiled_in": "5e6b6f1167f7",
    "release_date": "Wed Mar 2 10:34:48 UTC 2022",
    "machine": "x86_64",
    "doc": "https://fiware-orion.rtfd.io/en/3.6.0/",
    "libversions": {
      "boost": "1_66",
      "libcurl": "libcurl/7.61.1 OpenSSL/1.1.1k zlib/1.2.11 nghttp2/1.33.0",
      "libmosquitto": "2.0.12",
      "libmicrohttpd": "0.9.70",
      "openssl": "1.1",
      "rapidjson": "1.1.0",
      "mongoc": "1.17.4",
      "bson": "1.17.4"
    }
  }
}
```

## Criar entidade no Orion Context Broker. 

Para criar uma entidade no Orion Context Broker utilize o comando
    
```bash
curl -X POST \
  'http://localhost:1026/v2/entities/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --header 'fiware-service: openiot' \
  --header 'fiware-servicepath: /' \
  --data-raw '{
  "id": "urn:ngsi-ld:Store:001",
  "type": "Store",
  "address": {
    "type": "PostalAddress",
    "value": {
      "streetAddress": "Bornholmer Straße 65",
      "addressRegion": "Berlin",
      "addressLocality": "Prenzlauer Berg",
      "postalCode": "10439"
    },
    "metadata": {
      "verified": {
        "value": true,
        "type": "Boolean"
      }
    }
  },
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [
        13.3986,
        52.5547
      ]
    }
  },
  "name": {
    "type": "Text",
    "value": "Bösebrücke Einkauf"
  }
}'
```

Nota-se que os cabeçalhos `fiware-service` e `fiware-servicepath` são obrigatórios e indicam o serviço e caminho para o qual se deseja obter as entidades. Com isso as entidades de um serviço são transparentes para outro serviço. 

## Obter entidades do Orion Context Broker

Para obter as entidades do Orion Context Broker utilize o seguinte comando: 

```bash
curl -X GET \
  'http://localhost:1026/v2/entities/' \
  --header 'Accept: */*' \
  --header 'fiware-service: openiot' \
  --header 'fiware-servicepath: /'
```

A resposta obtida pode ser algo como:

```json
[
  {
    "id": "urn:ngsi-ld:Store:001",
    "type": "Store",
    "address": {
      "type": "PostalAddress",
      "value": {
        "streetAddress": "Bornholmer Straße 65",
        "addressRegion": "Berlin",
        "addressLocality": "Prenzlauer Berg",
        "postalCode": "10439"
      },
      "metadata": {
        "verified": {
          "type": "Boolean",
          "value": true
        }
      }
    },
    "location": {
      "type": "geo:json",
      "value": {
        "type": "Point",
        "coordinates": [
          13.3986,
          52.5547
        ]
      },
      "metadata": {}
    },
    "name": {
      "type": "Text",
      "value": "Bösebrücke Einkauf",
      "metadata": {}
    }
  }
]
```

Também é possível modificar e filtrar a resposta obtida utilizando-se os seguintes parametros de busca: 

| Parametro | valor | Descrição|
| --------- | --------- | -----------|
| options | keyvalues| Resume os valores de resposta
| type | Tipo da entidade | Filtra as entidades de determinado tipo 
| attrs | Limite de entidades | Filtra as entidades por determinado atributo
| q | Offset de entidades | Filtra as entidades por um valor de determinado atributo

Como exemplo pode-se filtrar a entidade acima utilizado a seguinte requisição:

```bash
curl -X GET \
  'http://localhost:1026/v2/entities/?options=keyValues&type=Store&q=name==Bösebrücke Einkauf&attrs=address' \
  --header 'Accept: */*' \
  --header 'fiware-service: openiot' \
  --header 'fiware-servicepath: /'
```

Obten-se a resposta:
```json
[
  {
    "id": "urn:ngsi-ld:Store:001",
    "type": "Store",
    "address": {
      "streetAddress": "Bornholmer Straße 65",
      "addressRegion": "Berlin",
      "addressLocality": "Prenzlauer Berg",
      "postalCode": "10439"
    }
  }
]
```

# Comandos para o IoT Agent JSON

## Obter informações do IoT Agent

Utilize a seguinte requisição:

```bash
curl -X GET \
  'http://localhost:4041/iot/about' \
  --header 'Accept: */*' \
```

Obtem-se a seguinte resposta:

```json
{
  "libVersion": "2.20.0",
  "port": "4041",
  "baseRoot": "/",
  "version": "1.21.1"
}
```

## Prover um serviço para o IoT Agent JSON

Utilize a seguinte requisição: 

```bash
curl -X POST \
  'http://localhost:4041/iot/services' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
  --header 'fiware-service: openiot' \
  --header 'fiware-servicepath: /' \
  --header 'Content-Type: application/json' \
  --data-raw '{
 "services": [
   {
     "apikey":      "security_information",
     "cbroker":     "http://orion:1026",
     "entity_type": "Device",
     "resource":    "/iot/json"
   }
 ]
}'
```

Nota-se que é necessário enviar no corpo da mensagem os seguintes parâmetros: ```apikey``` que é utilizado para autenticar a comunicação com os dispositivos e o Orion Context Broker, ```cbroker``` que é o endereço do Orion Context Broker, ```entity_type``` que é o tipo de entidade que será utilizado para a comunicação e ```resource``` que é o endereço padrão para recerber dados dos dispositivos.

## Providenciando um atuador para o IoT Agent JSON

Para providenciar um dispositivo para o IoT Agent JSON utilize a seguinte requisição:

```bash
curl -X POST \
  'http://iotagent:4041/iot/devices' \
  --header 'Accept: */*' \
  --header 'fiware-service: openiot' \
  --header 'fiware-servicepath: /' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "devices": [
    {
      "device_id": "Device1",
      "entity_name": "urn:ngsi-ld:Device:001",
      "entity_type": "Device",
      "transport": "HTTP",
      "endpoint": "http://endereço:porta/",
      "commands": [
        {
          "name": "on",
          "type": "command"
        },
        {
            "name": "off",
            "type": "command"
        }
      ],
      "static_attributes": []
    }
  ]
}'
```

Este dispositivo é capaz de receber os comandos ```on``` e ```off``` através do IoT Agent JSON. QUando solicitado, o IoT AGent JSON envia uma requisição HTTP para o endpoint especificado no campo ```endpoint``` do dispositivo. No Caso da versão 1 este endpoint é o do servidor web utilizando o Django. 

## Deletar um dispositivo no IoT Agent JSON

Para deletar um dispositivo no IoT Agent JSON é necessário saber o ID do dispositivo que será deletado. Para deletar o dispositivo utilize a requisição:

```bash
curl -X DELETE \
  'http://localhost:4041/iot/devices/Device_ID' \
  --header 'Accept: */*' \
  --header 'fiware-service: openiot' \
  --header 'fiware-servicepath: /' \
  --header 'Content-Type: application/json'
```