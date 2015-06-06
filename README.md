# kad.py

Python3 implementation of the Kademlia DHT data store.

Useful for distributing a key-value store in a decentralized manner.

To create a new DHT swarm, just call DHT() with the host and port that you will listen on. To join an existing DHT swarm, also provide bootstrap host and port numbers of any existing node.  The nodes will discover the rest of the swarm as appropriate during usage.


## Example: A two-node DHT

```python
from kad import DHT

host1, port1 = 'localhost', 3000
dht1 = DHT(host1, port1)
host2, port2 = 'localhost', 3001
dht2 = DHT(host2, port2, bootstrap_nodes=[(host1, port1)])
dht1["my_key"] = [u"My", u"json-serializable", u"Object"]

print (dht2["my_key"])	# blocking get
dht2.get ("my_key", lambda data: print (data)) # threaded get
```


## Example: Persistent storage

We can use a custom storage for local data. Storage parameter must an object with __getitem__ and __setitem__.
In this example we use shelve to create a persistent storage.

```python
from kad import DHT
import shelve

host, port = 'localhost', 3000
dht = DHT(host, port, storage=shelve.open ('sto.dat'))
```


## Example: Custom hash function

By default, kad.py doesn't hash keys. We can provide a custom hash_function.

```python
from kad import DHT

host, port = 'localhost', 3000
dht = DHT(host, port, hash_function=lambda d: d[0:4])
```
