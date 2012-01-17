import puka

AMQP_URL = "amqps:///"

client = puka.Client(AMQP_URL)
promise = client.connect()
client.wait(promise)

client.wait(client.close())
