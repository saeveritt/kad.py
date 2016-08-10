from kad import DHT
from json import loads
from urllib.request import urlopen
from time import sleep
from subprocess import Popen, PIPE
from hashlib import sha256
from peerassets import issue_tx, verify_owner
from operator import xor


host1,port1 = 'localhost',1234  #seed address and port
host2,port2 = 'localhost',1235  #your address and port

data = Popen(['ppcoind','getnewaddress'],stdout=PIPE,stderr=PIPE)
address,stderr = data.communicate()
address256 = sha256(address).hexdigest()

#Requires address to have 200 quantity of hopium in order to be considered as a valid entry
issuer = 'token issuer address'
name = 'hopium' 
qnt =  200

test = verify_owner(address,issuer, name, qnt)

if test == True:
        # Creating transaction by sending peerasset to newly created address and returns txid
        txid = issue_tx(address,'name:%s,qnt:%s'%(name,qnt))
else:
        print('Address does not own %s units of %s'%(qnt,name))

#For an entry to be valid there must be X amount of Y peerasset in address. This will transaction will be signed by owner. 
nodeid = xor(txid,address256)

dht = DHT(host2,port2,id=nodeid,seeds=[(host1,port1)])

#append some data to dht
key = sha256('some key' + 'salt').hexdigest()
dht[key] = 'unka unka'
