#from amqplib_client import *
from pika_client import *
from ticker_system import *

#publisher = PyAmqpLibPublisher(exchange_name="my_exchange")
publisher = PikaPublisher(exchange_name="my_exchange")
ticker = Ticker(publisher, "")
ticker.monitor()

