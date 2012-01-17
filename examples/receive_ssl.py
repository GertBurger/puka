#!/usr/bin/env python

"""
receive.py modified to show the use of SSL.
"""

import sys
sys.path.append("..")

import puka


client = puka.Client("amqps://127.0.0.1/")
promise = client.connect()
client.wait(promise)

promise = client.queue_declare(queue='test')
client.wait(promise)

print "  [*] Waiting for messages. Press CTRL+C to quit."

consume_promise = client.basic_consume(queue='test', prefetch_count=1)
while True:
    result = client.wait(consume_promise)
    print " [x] Received message %r" % (result,)
    client.basic_ack(result)

promise = client.close()
client.wait(promise)

