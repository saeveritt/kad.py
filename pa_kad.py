from kad import DHT
from hashlib import sha256
from peerassets import proven_txid, verify_owner
from operator import xor


host1,port1 = 'seed_address',1234  #seed address and port
host2,port2 = 'localhost',1235  #your address and port

address = 'public address in ownership of required PeerAsset'
address256 = sha256(address).hexdigest()

# Requires address to have a minimum quantity of 200 hopium in order to be considered as a valid entry
issuer = 'token issuer public address'
name = 'hopium' 
qnt =  200

# Returns True or False whether or not a given address owns the minumum amount of required PeerAsset
test = verify_owner(address,issuer, name, qnt)

if test == True:
        # Creating transaction by sending peerasset to newly created address and returns txid
        # proven_txid() returns the transaction id stating peerasset ownership
        # For an entry to be valid there must be X amount of Y peerasset in address. This transaction will be signed by owner. 
        txid = proven_txid(address,'issuer:%s,name:%s,qnt:%s'%(issuer,name,qnt))
else:
        print('%s does not own %s units of %s issued by %s'%(address,qnt,name,issuer))

nodeid = xor(txid,address256)
# node can be found by taking the xor of  the proven txid hash and hash of public address
dht = DHT(host2,port2,id=nodeid,seeds=[(host1,port1)])

#append some data to dht
key = sha256('some key' + 'salt').hexdigest()
#include transactionid for verification
dht[key] = txid + 'unka unka'
