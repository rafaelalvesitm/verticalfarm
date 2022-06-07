# Fazenda Vertical

Este é um projeto de pesquisa desenvolvido no [Centro Universitário FEI](https://portal.fei.edu.br/) iniciado em 2022. Este projeto visa desenvolver uma torre de cultivo monitorada, controlada e otimizada utilizando as tecnologias habilitadoras da Internet das Coisas e da Inteligência Artificial.

# Plataforma

A plataforma é composta pelos seguintes componentes:

- [Orion Context Broker](https://github.com/telefonicaid/fiware-orion/) - Gerenciador de contexto. 
- [IoT Agent JSON](https://github.com/telefonicaid/iotagent-json/blob/master/README.md) - Agente de IoT que traduz o protocolo JSON para o NGSI-V2 utilizad no Orion Context Broker
- [MongoDB](https://www.mongodb.com/) - Banco de dados não relacional.
- [PostgreSQL](https://www.postgresql.org/) - Banco de dados relacional. 
- [Cygnus](https://github.com/telefonicaid/fiware-cygnus) - Conector para persitir os dados no banco de dados.
- [Grafana](https://grafana.com/) - Visualização dos dados.
- [Web-application](https://www.djangoproject.com/) - Aplicação web para visualização dos dados e acionamento de atuadores. 

# Como a plataforma funciona? 

> Em desenvolvimento

# Como colocar a plataforma para funcionar? 

Para colocar a plataforma para funcionar, considerando o cenário de aplicação descrito anteriormente, abra a pasta [platform] no terminal e execute o comando:

```bash
$ ./setup.sh start
```