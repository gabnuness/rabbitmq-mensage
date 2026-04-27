import pika


class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self._host = "localhost"
        self.__port = 5672
        self.__username = "guest"  # todos os parâmetros
        self.__password = "guest"
        self.__queue = "my_queue"
        self.__callback = callback  # função para tratar os dados recebidos do RabbitMq
        self.__channel = self.__create_channel()


    # Criação do canal
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

rabbitmq_consumer = RabbitmqConsumer(minha_callback)
rabbitmq_consumer.start()