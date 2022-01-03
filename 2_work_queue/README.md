# Work Queue Tutorial

## Introduction to project

* * *

* Create a 'Work Queue' that will be used to distribute time-consuming task among multiple workers.
* The main idea is to avoid doing a resource-intensive task immediately and having to wait for it to complete. Instead, we schedule the task to be done later.
* Use time.sleep() function just to pretend that we are busy.
* To indicate how complex the tasks are, we will use '.' character that means it takes 1 second to be done.

## Source

* * *

* [Work Queue Tutorial][https://www.rabbitmq.com/tutorials/tutorial-two-python.html]

## Note

* * *

* If a consumer dies (its channel is closed, connection is closed or TCP connection is lost) without sending an ack(nowledgement), RabbitMQ will understand that a message wasn't processed fully and will re-queue it.

* If there are other consumers online at the same time, it will then quickly redeliver the message to another consumer.

* In this way, no messages are lost, even if the workers occasionally die.

* The task will also still be lost if RabbitMQ server stops or dies.

* When RabbitMQ quits or crashes, it will forget the queues and messages unless we tell it not to.

* To make sure that messages aren't lost, we need to mark both queue and messages as "durable". That is, we need to make both queue and messages persistent.

* If every odd tasks are heavy and the even are light, one worker will be constantly busy and the other one will relatively doesn't (Remeber wiaht Round Robin is).

* This happen because RabbitMQ just dispatches a message when the message enters the queue and it doesn't look at the number of unacknowledged messages for a consumer.

* In order to defeat this situation, we need to make the broker don't dispatch a new message to a worker until the previously-sent message processed and receive an acknowledgment of it.
