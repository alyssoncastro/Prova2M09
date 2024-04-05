from kafka import KafkaProducer
import json
import time
import random

#carregando o jason
with open('config.json') as f:
    config = json.load(f)


bootstrap_servers = config['bootstrap_servers']
topic = config['topic']


def generate_sensor_data():
    sensor_id = "sensor_001"
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    pollutants = ["PM2.5", "PM10", "CO2", "SO2"]
    pollutant = random.choice(pollutants)
    level = round(random.uniform(0, 100), 2)
    return {
        "idSensor": sensor_id,
        "timestamp": timestamp,
        "tipoPoluente": pollutant,
        "nivel": level
    }


def send_data():
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=lambda x: 
                             json.dumps(x).encode('utf-8'))
    
    
    
    while True:
        data = generate_sensor_data()
        producer.send(topic, value=data)
        print("Dados enviados:", data)
        time.sleep(1)



if __name__ == "__main__":
    send_data()
