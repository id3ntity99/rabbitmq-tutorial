import pika
import os
import sys


class Upper:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="to_upper", durable=True)

    def callback(self, ch, method, props, body):
        print(" [x] Received %r" % body.decode())
        print(" [x] Processing...")
        processed_msg = body.decode().upper()
        print(" [@] Done : %r" % processed_msg)
        # Send acknowledgment to queue
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume(self):
        self.channel.basic_consume(queue="to_upper", on_message_callback=self.callback)
        print(" [*] Waiting for messages... To exit press CTRL+C")
        self.channel.start_consuming()


def main():
    upper = Upper()
    upper.consume()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interrupted... Shuting down program")
        try:
            sys.exit(0)
        except SystemExit:
            print("Program shut down gracefully")
            os._exit(0)
