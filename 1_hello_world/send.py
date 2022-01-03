# Producer
import pika


class Producer:
    def __init__(self):
        # Connect to message broker
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        # Open channel
        self.channel = self.connection.channel()
        # Create receiving queue
        self.channel.queue_declare(queue="hello")

    def publish(self, msg):
        # Publish message to the queue using Default Exchange type.
        self.channel.basic_publish(exchange="", routing_key="hello", body=msg)
        print('[x] Sent "Hello World!"')
        # Close connection with message broker
        self.connection.close()


producer = Producer()
producer.publish("Hello World")
