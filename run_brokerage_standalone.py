#from amqplib_client import *
from pika_client import *
from buy_low_sell_high import *

#publisher = PyAmqpLibPublisher(exchange_name="my_exchange")
publisher = PikaPublisher(exchange_name="my_exchange")
buyer = Buyer(publisher, "", trend=25)
print "Buyer = %s" % id(buyer)
buyer.monitor()
