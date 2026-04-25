import pika


class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self._host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "gest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.create_channel()




    def __create_channel(self):
        # Parâmetros de Inicialização do RabbitMQ
        connection_parameters = pika.ConnectionParameters(  
            host=self._host,
            port=self.__port,              
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        # Criando canal
        channel = pika.BlockingConnection(connection_parameters).channel()

        # Declarando fila
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )

        # Como a queue(fila) será consumida
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback              
            # para onde irá as informações, uma ação condicional que ocorre quando chega a mensagem
        )

        return channel
    
    def start(self):
        print(f"Listen RabbitMQ on Port 5672")
        self.__channel.start_consuming()

def minha_callback(ch, method, proerties, body):
    print(body)