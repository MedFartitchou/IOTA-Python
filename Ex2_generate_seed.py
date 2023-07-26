#IOTA protocol: 81-tryte seed derives all private keys for one account. Generate it using SHA256 on os.urandom().
import os
import hashlib

rnd_seed = hashlib.sha256(os.urandom(256)).hexdigest()
print(rnd_seed)
