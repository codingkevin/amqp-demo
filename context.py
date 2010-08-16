from springpython.context import *
from springpython.config import *

from pika_client import *
from amqplib_client import *
from ticker_system import *
from buy_low_sell_high import *

class AppContext(PythonConfig):
    def __init__(self):
        PythonConfig.__init__(self)
        self.exchange_name = "my_exchange"

    @Object(scope.PROTOTYPE, lazy_init=True)
    def rabbitmq_publisher(self):
        #return PikaPublisher(exchange_name=self.exchange_name)
        return PyAmqpLibPublisher(exchange_name=self.exchange_name)

    @Object(scope.PROTOTYPE, lazy_init=True)
    def rabbitmq_listener(self):
        buyer = Buyer(self.rabbitmq_publisher(), "", trend=25)
        print "Buyer = %s" % id(buyer)
        return buyer

    @Object(scope.PROTOTYPE, lazy_init=True)
    def ticker(self):
        return Ticker(self.rabbitmq_publisher(), "")
