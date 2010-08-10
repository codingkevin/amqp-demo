import pickle
import random
import sys
import time

class Ticker(object):
    def __init__(self, publisher, qname):
        self.publisher = publisher
        self.stock_symbols = ["VMW", "S2", "VNX", "GOOGLE"]
        self.last_quote = {}
        self.counter = 0
        self.time_format = "%a, %d %b %Y %H:%M:%S +0000"
        self.qname = qname

    def get_quote(self):
        symbol = random.choice(self.stock_symbols)
        if symbol in self.last_quote:
            previous_quote = self.last_quote[symbol]
            new_quote = random.uniform(0.9*previous_quote, 1.1*previous_quote)
            if abs(new_quote) - 0 < 1.0:
                new_quote = 1.0
            self.last_quote[symbol] = new_quote
        else:
            new_quote = random.uniform(10.0, 250.0)
            self.last_quote[symbol] = new_quote
        self.counter += 1
        return (symbol, self.last_quote[symbol], time.gmtime(), self.counter)
   

    def monitor(self):
        while True:
            quote = self.get_quote()
            print("New quote is %s" % str(quote))
            self.publisher.publish(pickle.dumps((quote[0], quote[1], time.strftime(self.time_format, quote[2]), quote[3])), routing_key="")
            secs = random.randint(1,5)
            #print("Sleeping %s seconds..." % secs)
            time.sleep(secs)
        
