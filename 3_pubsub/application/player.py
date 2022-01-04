import pika
import sys
import os


class Player:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue="", exclusive=True)
        self.queue_name = result.method.queue
        self._name = sys.argv[1]
        self._hp = int(sys.argv[2])

    def _callback(self, ch, method, props, body):
        self._hp -= int(body)
        print("%r has been damaged! HP remains: %r" % (self._name, self._hp))

        if self._hp <= 0:
            print("GAME OVER! %r died..." % self._name)
            try:
                print("Exit game")
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def take_attack(self):
        self.channel.queue_bind(exchange="battle", queue=self.queue_name)
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self._callback, auto_ack=True
        )
        print(" [*] Get ready for the attack..!! (To quit, press CTRL+C)")
        self.channel.start_consuming()


def main():
    player = Player()
    player.take_attack()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
