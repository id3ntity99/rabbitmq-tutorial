import sys
import os
import pika


class Receive:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        # Create fanout-exchange with the name of logs
        # in case of no such an exchange exists
        self.channel.exchange_declare(exchange="logs", exchange_type="fanout")
        # Create randomly-named queue and automatically delete the queue
        # when the connection to the consumer is closed
        result = self.channel.queue_declare(queue="", exclusive=True)
        # Get the name of queue
        self.queue_name = result.method.queue

    def _callback(self, ch, method, props, body):
        print(" [x] Received %r" % body)

    def consume(self):
        # Bind the queue to logs exchange
        self.channel.queue_bind(exchange="logs", queue=self.queue_name)
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self._callback, auto_ack=True
        )
        print(" [*] Waiting for messages... To exit press CTRL+C")
        self.channel.start_consuming()


def main():
    receiver = Receive()
    receiver.consume()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
