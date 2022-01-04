# Publish/Subscribe Tutorial

## Introduction to project

- Previous tutorial project, Work Queue, is that each task is delivered to exactly one worker.

- In this tutorial project, we'll deliver one message to multiple consuers using 'publish/subscribe pattern'.

- To illustrate the pattern, we're going to build a simple logging system that will consist of two programs - the first will emit log messages and the second will receive and print them.

- In the logging system, every running receiver program will get the messages. One receiver program will receive a log and direct the it to disk, and the other, at the same time, will display log on the screen.

- Essentially, published log messages are going to be broadcast to all the receivers.

## Source

- Publish/Subscribe Tutorial: https://www.rabbitmq.com/tutorials/tutorial-three-python.html

## Note

### Exchanges

- In previous tutorial project, the messages are sent and received to and from a queue. Now it's time to introduce the full messaging model in RabbitMQ.

- The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. Instead, the producer can only send messages to an exchange.

- On one side of an exchange, it receives messages from producers and the other side it pushes them to queues.

- The exchange must know exactly what to do with a message it receives, such as should it be appended to a particular queue? Should it be appended to multiple queues? Or shuold it get discarded?

- The answers are defined by the exchange type.(Direct, topic, headers, fanout) And we're going to use fanout exchange type for this tutorial

- The fanout exchange is proper to broadcast all the messages to all of the queues that bound to the exchange.

- Also, fanout exchange ignores routing keys, thus, we don't need to provide routing key to the exchange as an attribute.

### Temporary Queues

- 몇 개의 큐가 exchange에 바인딩 될 지 모르므로 컨슈머 측에서 무작위 이름을 가진 큐를 직접 생성.
- exclusive를 True로 하지 않으면 컨슈머가 실행될때 생성된 큐가 컨슈머 종료 후에도 남아있음. exclusive를 True로 할 경우 컨슈머가 실행될 때 큐가 생성되고 종료할 때 큐도 같이 제거됨.
