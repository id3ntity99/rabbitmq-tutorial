# Producer
import pika
import sys


class Producer:
    def __init__(self):
        # Connect to the broker
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        # Open channel
        self.channel = self.connection.channel()
        # Make queue durable
        # This will make queue keep alive even if the broker dies
        self.channel.queue_declare(queue="task_queue", durable=True)

    def publish(self):
        message = " ".join(sys.argv[1:]) or "Hello World!"
        self.channel.basic_publish(
            exchange="",
            routing_key="task_queue",
            body=message,
            # Make messages persistent
            # This will make messages keep alive even if the broker dies
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        print(" [x] Sent %r" % message)
        self.connection.close()


def main():
    producer = Producer()
    producer.publish()


if __name__ == "__main__":
    main()
