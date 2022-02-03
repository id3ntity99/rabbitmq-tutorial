import pika
import uuid
import os
import sys


class Client(object):
    def __init__(self):
        self._open_channel()
        self._craete_queue()
        self.channel.basic_consume(
            queue=self.callback_queue_name,
            on_message_callback=self._on_response,
            auto_ack=True,
        )

    def _craete_queue(self):
        # Create random-name exclusive queue
        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue_name = result.method.queue

    def _open_channel(self):
        connection_param = pika.ConnectionParameters("localhost")
        self.connection = pika.BlockingConnection(connection_param)
        self.channel = self.connection.channel()

    def _on_response(self, ch, method, props, body):
        # If the response cid matches to the request cid
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",
            # The properties will tell the server where to send response
            # Server will send response to the callback queue
            # that client created
            properties=pika.BasicProperties(
                reply_to=self.callback_queue_name, correlation_id=self.corr_id
            ),
            body=str(n),
        )
        while self.response is None:
            # process_data_events() will make sure that
            # data events are processed
            # In short, it will check wether data processed
            self.connection.process_data_events()
        return int(self.response)


def main():
    rpc_client = Client()
    print(" [x] Requesting fib(30)")
    response = rpc_client.call(30)
    print(" [.] Got %r" % response)


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
