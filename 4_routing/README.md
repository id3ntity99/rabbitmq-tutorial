# Routing Tutorial

## Introduction to project

- In the previous tutorial, we were able to broadcast log messages to multiple receivers.

- In this tutorial, we're going to add a feature to it - we're going to make it possible to subscribe only to a subset of the messages.

- For example, we will be able to driect only critical error messages to the log file, while still being able to print all of the log messages.

## Source

- Routing Tutorial: https://www.rabbitmq.com/tutorials/tutorial-four-python.html

## Note

### Bindings

- A biding is a relationship between an exchange and a queue, which can be read as "the queue is interested in messages from this exchange".

- The binding can also have routing_key attribute, just like queue does, and the key depends on the exchange type.The fanout exchanges, which was used previously, ignored the value of the routing_key so it wasn't necessary.

### Direct exchange

- The logging system from the previous tutorial broadcasts all messages to all consumers.

- We used a fanout exchange for the logging system, which doesn't give too much flexibility, thus we'are going to use a 'direct exchange' to filter messages.

- The routing algorithm behind a direct exchange is simple - a message goes to the queues whose binding key exactly matches to routing key of the messages.

### Multiple bindings

- One of the keys is use multiple bindings to filter messages.

- If a message that is published to the exchange with the certain routing key, the message will be sent to that queue with the same binding key.

- Also, it is perfectly legal to bind multiple queues with the same biding key.
  In this case, the exchange will behave like fanout exchange, even though it is direct exchange, and will broadcast the message to all the matching queues.
