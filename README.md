# 📬RabbitMQ (Mensageria)

## 📖 Sobre o projeto

Este repositório foi criado com o objetivo de aprender e praticar o uso do **RabbitMQ** como ferramenta de mensageria.

Entender na prática, como sistemas podem se comunicar de forma **assíncrona**, desacoplada e escalável.

---

## 🚀 Por que usar RabbitMQ?

Em aplicações tradicionais, é comum que sistemas se comuniquem de forma direta (ex: API → API). Isso pode gerar:

* Alto acoplamento entre serviços
* Baixa escalabilidade
* Dificuldade em lidar com falhas

O RabbitMQ resolve esses problemas ao introduzir um intermediário (broker de mensagens), permitindo:

* 📩 Comunicação assíncrona
* 🔗 Desacoplamento entre produtor e consumidor
* ⚖️ Melhor distribuição de carga
* 🛡️ Maior resiliência a falhas

---

## 🧠 Conceitos principais

* **Producer (Publisher)**: responsável por enviar mensagens
* **Queue (Fila)**: onde as mensagens ficam armazenadas
* **Consumer**: responsável por processar as mensagens
* **Broker (RabbitMQ)**: gerencia o fluxo das mensagens
