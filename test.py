from kad import DHT


"""
dhts = []
hosts = []
port = 3000

for x in range (0, 10):
	nhost = ('localhost', port)

	if len (hosts) == 0:
		ndht = DHT (nhost[0], nhost[1])
	else:
		rhost = random.choice (hosts)
		ndht = DHT (nhost[0], nhost[1], boot_host=rhost[0], boot_port=rhost[1])

	hosts.append (nhost)
	dhts.append (ndht)
	port += 1

testo = ["My", "json-serializable", "Object"]
random.choice (dhts)["my_key"] = testo

for x in range (0, 1):
	assert (random.choice (dhts)["my_key"] == testo)
	
"""



host1, port1 = 'localhost', 3000
dht1 = DHT(host1, port1)

host2, port2 = 'localhost', 3001
dht2 = DHT(host2, port2, bootstrap_nodes=[(host1,port1)])

dht1["my_key"] = [u"My", u"json-serializable", u"Object"]

dht2.get ("my_key", lambda d: print ('Find:',d))
#print (dht2["my_key"])
