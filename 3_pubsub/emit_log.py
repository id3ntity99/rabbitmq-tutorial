import pika
import sys
import os


class Producer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        # Decalre the exchange with the name of 'logs'
        # and the type of "fanout"
        self.channel.exchange_declare(exchange="logs", exchange_type="fanout")

    def emit_log(self):
        message = " ".join(sys.argv[1:]) or "Info: Hello World!"
        # Fanout exchange doesn't require routing key
        self.channel.basic_publish(exchange="logs", routing_key="", body=message)
        print(" [x] Sent %r" % message)
        self.connection.close()


def main():
    log_emitter = Producer()
    log_emitter.emit_log()


if __name__ == "__main__":
    main()
