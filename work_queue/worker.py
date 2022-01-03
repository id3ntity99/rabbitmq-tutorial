import pika
import time
import os
import sys


class Consumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="task_queue", durable=True)

    def callback(self, ch, method, props, body):
        print(" [x] Received %r" % body.decode())
        time.sleep(body.count(b"."))
        print(" [x] Done")
        # Message acknowledgment turned on
        # Even if worker dies during its processing,
        # the message is still alive in queue
        # because queue doesn't recieve any ack from the worker
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue="task_queue", on_message_callback=self.callback
        )
        print(" [*] Waiting for messages... To exit press CTRL+C")
        self.channel.start_consuming()


def main():
    consumer = Consumer()
    consumer.consume()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
