import pika
import sys
import os


class Consumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue="", exclusive=True)
        self.queue_name = result.method.queue

    def _callback(self, ch, method, props, body):
        print(" [@] Log Received - %r:%r" % (method.routing_key, body))

    def consume(self):
        severities = sys.argv[1:]
        print(" [*] This consumer will receive %r errors only." % severities)
        # Bind queue to direct exchange with severity name as routing key
        for severity in severities:
            self.channel.queue_bind(
                exchange="direct_logs", queue=self.queue_name, routing_key=severity
            )
        print(" [*] Waiting for logs... To exit press CTRL+C")
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self._callback, auto_ack=True
        )
        self.channel.start_consuming()


def main():
    consumer = Consumer()
    consumer.consume()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n [x] Keyboard Interrupted... Shuting down program")
        try:
            sys.exit(0)
        except SystemExit:
            print(" [x] Program shut down gracefully")
            os._exit(0)
