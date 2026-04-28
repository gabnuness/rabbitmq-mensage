# 📬 Projeto de Estudo: RabbitMQ

## 📖 Sobre o projeto

Este repositório foi criado com o objetivo de aprender e praticar o uso do **RabbitMQ** como ferramenta de mensageria em aplicações distribuídas.

Para facilitar o ambiente e evitar configurações locais complexas, foi utilizado **Docker** para subir um container rodando o RabbitMQ.

A proposta principal é entender, na prática, como sistemas podem se comunicar de forma **assíncrona**.

---

## 🧠 Conceitos principais

* **Publisher**: responsável por enviar mensagens
* **Queue (Fila)**: onde as mensagens ficam armazenadas
* **Consumer**: responsável por processar as mensagens
* **Broker/Exchange (RabbitMQ)**: gerencia o fluxo das mensagens

---

## 🛠️ Estrutura do projeto

Durante o aprendizado, o desenvolvimento foi dividido em duas etapas:

### 🔹 1. Implementação simples (teste inicial)

Foram criados arquivos básicos apenas para validar o funcionamento da mensageria:

* `publisher_row.py`

  * Envia mensagens simples para a fila

* `consumer_row.py`

  * Consome e exibe mensagens da fila

---

### 🔹 2. Refatoração com POO

Após validar o funcionamento, o código foi refatorado utilizando **Programação Orientada a Objetos (POO)**:

* `publisher.py` 

 * Versão estruturada do publisher
 * Responsável por encapsular a lógica de envio de mensagens
 * Facilita reutilização e manutenção

* `consumer.py`

  * Versão mais organizada e reutilizável do consumer
  * Melhor separação de responsabilidades
  * Estrutura mais próxima de aplicações reais

---

## 🔄 Fluxo de funcionamento

1. O **publisher** envia uma mensagem
2. O RabbitMQ recebe e armazena na fila por meio de uma exchange
3. O **consumer** escuta a fila
4. Ao receber uma mensagem, o consumer processa o conteúdo

---

## 🎯 Objetivo

Este projeto tem como foco:

* Aprender os fundamentos de mensageria
* Entender o funcionamento do RabbitMQ na prática
* Utilizar Docker para gerenciamento de ambiente
* Evoluir de uma implementação simples para uma estrutura com POO
* Simular cenários reais de comunicação entre sistemas

---

## 🧪 Tecnologias utilizadas

* Python
* RabbitMQ
* Docker

---

> 💡 Projeto voltado exclusivamente para aprendizado e experimentação.
