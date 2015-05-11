from kad import DHT

host1, port1 = 'localhost', 3000
dht1 = DHT(host1, port1)

host2, port2 = 'localhost', 3001
dht2 = DHT(host2, port2, boot_host=host1, boot_port=port1)

dht1["my_key"] = [u"My", u"json-serializable", u"Object"]

print (dht2["my_key"])
