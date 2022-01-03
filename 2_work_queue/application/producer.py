import pika
import sys
import os


class Producer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        # Decalre persistent queue with the name of to_upper
        self.channel.queue_declare(queue="to_upper", durable=True)

    def publish(self):
        message = input(" [*] Input: ")
        # Publish a message to the queue 'to_upper'
        # Make message persistent
        self.channel.basic_publish(
            exchange="",
            routing_key="to_upper",
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        print(" [@] Sent %r" % message)
        self.connection.close()


def main():
    producer = Producer()
    print(" [*] Ready to send Message... To exit press CTRL+C")
    # Create infinite loop
    while True:
        producer.publish()


if __name__ == "__main__":
    try:
        main()
        # If user exit program, close connection to queue
        # and exit gracefully
    except KeyboardInterrupt:
        print("\nKeyboard Interrupted... Shuting down Program")
        try:
            sys.exit(0)
        except SystemExit:
            print("Program shut down gracefully")
            os._exit(0)
