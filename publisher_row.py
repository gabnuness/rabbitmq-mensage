import pika

# Declaração de Canal
connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)


channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="EstouMandandoUMaMensagem", # mensagem que será enviada
    properties=pika.BasicProperties(
        delivery_mode=2 # modo de entrega focada na entrega garantida ao invés da taxa de transferência
    )
)

