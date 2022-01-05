import pika
import sys


class Producer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange="topic_log", exchange_type="topic")

    def publish(self):
        routing_key = sys.argv[1] if len(sys.argv) > 2 else "anonymous.info"
        message = " ".join(sys.argv[2:]) or "Hello World!"
        self.channel.basic_publish(
            exchange="topic_log", routing_key=routing_key, body=message
        )
        print(" [x] Sent %r:%r" % (routing_key, message))
        self.connection.close()


def main():
    producer = Producer()
    producer.publish()


if __name__ == "__main__":
    main()
