#!/usr/bin/env python

import sys
sys.path.append("..")


import puka

client = puka.Client("amqp://localhost/")

ticket = client.connect()
client.wait(ticket)

ticket = client.queue_declare(queue='test')
client.wait(ticket)

ticket = client.basic_publish(exchange='', routing_key='test',
                              body="Hello world!")
client.wait(ticket)

print " [*] Message sent"

ticket = client.close()
client.wait(ticket)
