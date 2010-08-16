from amqplib import client_0_8 as amqp

class PyAmqpLibPublisher(object):
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.exchange_exists = False
        self.queue_exists = False

    def publish(self, message, routing_key):
        conn = amqp.Connection(host="127.0.0.1", userid="guest", password="guest", virtual_host="/", insist=False)

        ch = conn.channel()

        if not self.exchange_exists:
            print "Creating fanout exchange %s" % self.exchange_name
            ch.exchange_declare(exchange=self.exchange_name, type="fanout", durable=False, auto_delete=False)
            self.exchange_exists = True

        msg = amqp.Message(message)
        msg.properties["content_type"] = "text/plain"
        msg.properties["delivery_mode"] = 2
        ch.basic_publish(exchange=self.exchange_name,
                         routing_key=routing_key,
                         msg=msg)
        ch.close()
        conn.close()
    
    def monitor(self, qname, callback):
        conn = amqp.Connection(host="127.0.0.1", userid="guest", password="guest")

        ch = conn.channel()

        if not self.queue_exists:
            ch.queue_declare(queue=qname, durable=False, exclusive=False, auto_delete=False)
            ch.queue_bind(queue=qname, exchange=self.exchange_name)
            print "Binding queue %s to exchange %s" % (qname, self.exchange_name)
            #ch.queue_bind(queue=qname, exchange=self.exchange_name, routing_key=qname)
            self.queue_exists = True

        ch.basic_consume(callback=callback, queue=qname)

        while True:
            ch.wait()
        print 'Close reason:', conn.connection_close

