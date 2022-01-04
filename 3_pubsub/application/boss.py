import pika


class Boss:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange="battle", exchange_type="fanout")

    def attack(self, damage):
        message = damage
        self.channel.basic_publish(exchange="battle", routing_key="", body=message)
        print("Boss attacks all players!! (Damage: %r)" % message)
        self.connection.close()


def main():
    boss = Boss()
    boss.attack("10")


if __name__ == "__main__":
    main()
