import pika


def minha_callback(ch, method, proerties, body):
    print(body)

# Parâmetros de Inicialização do RabbitMQ
connection_parameters = pika.ConnectionParameters(  
    host="localhost",
    port=5672,              
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

# Criando canal
channel = pika.BlockingConnection(connection_parameters).channel()

# Declarando fila
channel.queue_declare(
    queue="my_queue",
    durable=True
)

# Como a queue(fila) será consumida
channel.basic_consume(
    queue="my_queue",
    auto_ack=True,
    on_message_callback=minha_callback              # para onde irá as informações, uma ação condicional que ocorre quando chega a mensagem
)

print(f"Listen RabbitMQ on Port 5672")
channel.start_consuming()