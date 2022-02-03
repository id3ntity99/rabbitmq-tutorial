import pika
import sys
import os


class Server:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        # This queue will accept incoming messages(requests)
        self.channel.queue_declare(queue="rpc_queue")

    def _fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self._fib(n - 1) + self._fib(n - 2)

    # Callback method that generates Fibonacci number
    # and publishes the number as response
    def on_request(self, ch, method, props, body):
        n = int(body)
        print(" [.] fib(%s)" % n)
        response = self._fib(n)
        # The resonse message will be routed to 'reply_to' callback queue
        # that declared by client and exclusive to it
        ch.basic_publish(
            exchange="",  # Use default exchange
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=str(response),
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def get_request(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue="rpc_queue", on_message_callback=self.on_request
        )
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()


def main():
    rpc_server = Server()
    rpc_server.get_request()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupted... Shuting down program")
        try:
            sys.exit(0)
        except SystemExit:
            print("Program shut down gracefully")
            os._exit(0)
