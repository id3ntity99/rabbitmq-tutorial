# Consumer
import pika
import os
import sys


class Consumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        # Declare queue again because to make  sure
        # that the queue already exists.
        self.channel.queue_declare(queue="hello")

    # Subscribe callback function to a queue.
    # Whenever receive a message, this callback function is called
    # by the Pika library.
    def callback(self, ch, method, props, body):
        print(" [x] Received %r" % body)

    def consume(self):
        self.channel.basic_consume(
            queue="hello", auto_ack=True, on_message_callback=self.callback
        )
        print("[*]Waiting for messages...To exit press CTRL+C")
        # Never-ending loop that waits for data and
        # runs callbacks whenever necessary.
        self.channel.start_consuming()


if __name__ == "__main__":
    try:
        consumer = Consumer()
        consumer.consume()
    except KeyboardInterrupt:
        print("Keyboard Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
