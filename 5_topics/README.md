# Topics Tutorial

## Introduction to project

- The direct exchange, we previously used, let us gain a possibility of selectively receiving the logs.

- Although using the direct exchange improved logging system, it still ahs limitation - it can't do routing based on multiple criteria.

- In our loggin system, we might want to subscribe to not only logs based on severity, but also based on the source which emitted the log.

- Just like unix's 'syslog', for instance, we may want to listen to just critical errors coming from 'cron' but also all logs from 'kern'.

- To build this system, we need to learn about a more complex 'topic exchange'

## Note

### Topic exchange

- Messages sent to a topic exchange can't have an arbitrary routing_key, it must be a list of words, delimited by dots.

- The binding key must also be in the same form.

- The logic behind the topic exchange is similar to ta direct exchange - a message sent with a particular routing key will be delivered to all the queues that are bound with a matching binding key.
  But, there are two important special cases for binding keys:

- Asterisk can substitute for exactly one word. For example, if a binding key is \*.\*.red, then any routing key with .red will be routed to the queue witthat binding key.

- # can substitute for zero or more words. For example, a queue with a binding key blue.# will receive any messages whose routing_keys are blue.\*.\*

- Even though a routing key has four words, and has any matching keyword to certain bidiny key, it will be delivered to those queues.

- Topick exchange is powerful and can behave like other exchanges.

- When a queue is bound with hash binding key, it will receive all the messages, regardless of the routing key - like in fanout exchange.

- When special characters asterisk and hash aren't used in bindings, the topic exchange will behave just like a direct exchange.
