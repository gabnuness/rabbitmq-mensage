from typing import Dict
import pika 
import json

class RabbitmqPublisher:
    def __init__(self) -> None:
        self._host = "localhost"
        self.__port = 5672
        self.__username = "guest" 
        # queue removida pois o publisher só se comunica com a exchange
        self.__password = "guest"
        self.__exchange = "data_exchange"
        self.__routing_key = ""
        self.__channel = self.__create_channel()

    def __create_channel(self):
        # Declaração de Canal
        connection_parameters = pika.ConnectionParameters(
        host=self._host,
        port=self.__port,
        credentials=pika.PlainCredentials(
            username=self.__username,
            password=self.__password
        )
    )
        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel
    
    def send_message(self, body: Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body), # mensagem que será enviada
            properties=pika.BasicProperties(
                delivery_mode=2 # modo de entrega focada na entrega garantida ao invés da taxa de transferência
            )
        )

rabbitmq_publisher = RabbitmqPublisher()
rabbitmq_publisher.send_message({ "ola": "mundo"})
