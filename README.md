# Monitoramento de Qualidade do Ar com Apache Kafka

###### AUTOR: ALYSSON C. C. CORDEIRO - ENG. DA COMPUTAÇÃO

---

## Objetivo:

O objetivo é implementar um sistema de monitoramento de qualidade do ar utilizando Apache Kafka, o qual sistema consistirá em gerar dados simulados de sensores de qualidade do ar e enviá-los para um tópico do Kafka, onde serão consumidos e processados para exibição e armazenamento.

## E ideia da Atividade é o seguinte:

"Uma cidade está implementando um novo sistema de monitoramento de qualidade do ar, o qual consiste em diversos sensores espalhados pela cidade que captam níveis de poluentes em tempo real.  E os dados coletados pelos sensores precisam ser transmitidos para um sistema central de análise de dados para monitoramento e resposta rápida em caso de detecção de níveis perigosos de poluição. Por esse motivo, ao implementar o sistema, os especialistas perceberam que o sistema central é incapaz de processar muitas requisições para armazenamento de dados de sensores ao mesmo tempo e, quando o sistema alcança o seu limite, começa a perder dados enviados. Eu foi contratado para resolver esse problema. Para isso, eu utilizei o Apache Kafka para implementar uma fila de eventos e, assim, criar um amortecimento com persistência para que o sistema consiga absorver os momentos de pico sem perdas de dados."

## Tecnologias utilizadas:

- Python 
- ZooKeeper
- Apache Kafka
- Docker (para baixar e instalar o zookeeper)

## Instalações:

### 1. Docker:

Instale o Docker Desktop e o inicie. Execute o contêiner do Zookeeper abrindo o terminal do windowns

```python
docker run --name meu-zookeeper -p 2181:2181 -d zookeeper
```

### 2. Bibliotecas python

```python
pip install kafka-python
```

### 3. instalae e configure o Apache Kafka

Baixe-o, instale-o e extrai os arquivos. Inici o servidor Zookeeper:

```python
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```
Agora o Kafka:

```python
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

Vale ressaltar que os  arquvivos "producer.py" e "consumer.py" estão, respectivamente, responsáveis por gerar dados simulados de sensores de qualidade do ar e publicá-los em um tópico do Kafka, e outro de exibí-los.

## Execução:

Em terminais diferentes execeute: "python producer.py" e "python consumer.py"

## Testes:

No começo estava dendo certo, no entanto ao tentar finalizar ocorreu erros como um problema de 'zkServer.cmd' o qual não está sendo reconhecido como um comando interno, mesmo instalado e configurado no PATH, por exemplo. Sem contar que pode ta ocorrendo de algum problema com a instalação do pacote kafka-python., pois não reconhece mais alguns comando.




