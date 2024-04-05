from kafka import KafkaConsumer
import json

#carregando json
with open('config.json') as f:
    config = json.load(f)


bootstrap_servers = config['bootstrap_servers']
topic = config['topic']


def consume_data():
    consumer = KafkaConsumer(topic,
                             bootstrap_servers=bootstrap_servers,
                             auto_offset_reset='earliest',
                             group_id=None,
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    
    for message in consumer:
        data = message.value
        print("Dados recebidos:", data)


if __name__ == "__main__":
    consume_data()
