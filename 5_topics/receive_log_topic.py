import pika
import sys
import os


class Consumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange="topic_log", exchange_type="topic")
        result = self.channel.queue_declare("", exclusive=True)
        self.queue_name = result.method.queue

    def _callback(self, ch, method, props, body):
        print(" [x] Received %r:%r" % (method.routing_key, body))

    def consume(self):
        binding_keys = sys.argv[1:]
        if not binding_keys:
            sys.stderr.write("Usage:  %s [binding_key]...\n" % sys.argv[0])
            sys.exit(1)

        for binding_key in binding_keys:
            self.channel.queue_bind(
                exchange="topic_log", queue=self.queue_name, routing_key=binding_key
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
