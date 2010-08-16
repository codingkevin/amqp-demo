from springpython.context import *
from context import *

ctx = ApplicationContext(AppContext())
ctx.get_object("rabbitmq_listener").monitor()
