import pika
import sys
import os


class Producer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        # Declare direct exchange
        self.channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

    def close_channel(self):
        self.connection.close()

    def publish(self):
        # severity == 심각성
        # severity must identical to severities that are given by consumer
        severity = input(" [*] Severity: ")
        message = input(" [*] Input: ")
        self.channel.basic_publish(
            exchange="direct_logs",
            routing_key=severity,  # Set severity as routing key
            body=message,
        )
        print(" [@] Sent %r: %r" % (severity, message))


def main():
    producer = Producer()
    try:
        while True:
            producer.publish()
    except KeyboardInterrupt:
        producer.close_channel()
        print("\n [x] Keyboard Interrupted... Shuting down program")
        try:
            sys.exit(0)
        except SystemExit:
            print(" [x] Program shut down gracefully")
            os._exit(0)


if __name__ == "__main__":
    main()
