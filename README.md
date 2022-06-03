# Fazenda Vertical

Este é um projeto de pesquisa desenvolvido no [Centro Universitário FEI](https://portal.fei.edu.br/) iniciado em 2022. Este projeto visa desenvolver uma torre de cultivo monitorada, controlada e otimizada utilizando as tecnologias habilitadoras da Internet das Coisas e da Inteligência Artificial.

## Resumo do projeto

Em 2017, a Organização para a Alimentação e a Agricultura das Nações Unidas recomendou que os países se esforçassem para aumentar a produção de alimentos em 50% até 2050 em relação ao ano base de 2012, pois o aumento da população é crescente e a qualidade de vida tende a melhorar com o tempo. Muito são os esforços porém uma das possibilidades para superar esse grande desafio é a implementação de fazendas verticais de forma sustentável. Dentro desse contexto, a motivação deste projeto de pesquisa é o de contribuir com o agronegócio brasileiro e a segurança alimentar do nosso país e da população mundial por meio do uso da Internet das Coisas e da Inteligência Artificial visando potencializar a produção de cultivos em fazendas verticais. Assim sendo, o objetivo deste projeto de pesquisa é o de desenvolver um gêmeo digital (ferramenta que integra elementos físicos, como sensores e atuadores, a elementos digitais, como serviços na nuvem e inteligência artificial) para uma torre de cultivo de uma fazenda vertical. O uso de algoritmos evolucionários de inteligência artificial associado a inteligência humana (expertise do produtor) será utilizada para otimizar a produção de cultivos, por meio do monitoramento, do controle e do gerenciamento otimizado e robusto (tolerante às variações do ambiente e dos processos produtivos) das condições ambientais, do uso de insumos, do consumo de recursos hídricos e energéticos de uma torre de cultivo de uma fazenda vertical, para garantir que a produção de alimentos seja efetiva, eficaz, precisa, robusta e sustentável. 

## Integrantes

- Rafael Gomes Alves - Aluno de doutorado
- Salvador Pinillos Gimenez - Orientador
- Fabio Lima - Coorientador

## Plataforma 

Este projeto é desenvolvido com base na plataforma [FIWARE](https://fiware.org/). Recomenda-se realizar os tutorials disponíveis no site do FIWARE, em especial os tutoriais:

- [Getting Started](https://fiware-tutorials.readthedocs.io/en/latest/getting-started.html)  
- [Entity Relationships](https://fiware-tutorials.readthedocs.io/en/latest/entity-relationships.html)  
- [CRUD Operations](https://fiware-tutorials.readthedocs.io/en/latest/crud-operations.html)  
- [Context Providers](https://fiware-tutorials.readthedocs.io/en/latest/context-providers.html)  
- [Altering the Context Programmatically](https://fiware-tutorials.readthedocs.io/en/latest/accessing-context.html)  
- [Subscribing to Changes in Context](https://fiware-tutorials.readthedocs.io/en/latest/subscriptions.html)  
- [Introduction to IoT Sensors](https://fiware-tutorials.readthedocs.io/en/latest/iot-sensors.html)  
- [Provisioning an IoT Agent](https://fiware-tutorials.readthedocs.io/en/latest/iot-agent.html)  
- [Persisting Context Data using Apache Flume (MongoDB, MySQL, PostgreSQL)](https://fiware-tutorials.readthedocs.io/en/latest/historic-context-flume.html)  
- [Persisting Context Data using Apache NIFI (MongoDB, MySQL, PostgreSQL)](https://fiware-tutorials.readthedocs.io/en/latest/historic-context-nifi.html) 


## Versões de Treinamento e aprendizado

Cada versão da plataforma foi desenvolvida para testar um elemento da plataforma IoT. Assim o aprendizado é construido passo a passo e a complexidade aumenta conforme a versão.

- [Versão 1](./version1/README.md): Apresenta o funcionamento dos componentes básicos da plataforma incluindo o Orion Context Broker, o IoT Agent JSON, o MongoDB e um servidor web utilizando o Django. Todos os componentes estão incluindos em containers independentes ligados pela mesma rede de comunicação. Para a operação dos containers utiliza-se o Docker. 
- [Versão 2](./version2/README.md): Apresenta o funcionamento dos componentes básicos da plataforma incluindo o Orion Context Broker, o IoT Agent JSON, o MongoDB e uma Raspberry Pi 3 model B+ com um servidor web utilizando o Django. Todos os componentes com excessão da Raspberry Pi estão em containers independentes ligados pela mesma rede de comunicação. Para a operação dos containers utiliza-se o Docker. A configuração da Raspberry Pi é feita por SSH. 


## Versão final

A versão final da plataforma está disponível na pasta "platform" e as informações da plataforma estão defininas em [platform](./platform/README.md). A versão final ainda está em desenvolvimento e será detalhada em breve.