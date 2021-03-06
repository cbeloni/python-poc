import json
from kafka import KafkaConsumer


if __name__ == '__main__':
    
    consumer = KafkaConsumer(
        'msg',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest'        
    )
    
    for message in consumer:
        print(json.loads(message.value))
    