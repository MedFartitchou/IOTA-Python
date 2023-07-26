# In this example, a transaction is created with a custom index/data. 
# The specified amount of IOTA in the "amount" variable will be transferred to the provided address.

import iota_client

SENDER_SEED = 'a201599ad3bc079378e1e3cba43ee976828c146ec95f296c7d3a4ddc7dee24f37edba7b2bf8055503babd992964e0cb3649af6f184626636741cd9d6813b8c57'
RECIPIENT_ADDRESS = 'atoi1qz8wn7fj23g3qz8rpk9dk38zffs6u7wmdalvu7eak8a5r7me72pw2vspcl0'
INDEX = "IOTA Network"
DATA = "IOTA tokens!".encode()
client = iota_client.Client( nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])
output = {
    'address': RECIPIENT_ADDRESS,
    'amount': 2000000  # 2 MIOTA
}
message_id = client.message(seed=SENDER_SEED, index=INDEX, data=DATA, outputs=[output])
print(f"IOTAs sent!\n https://explorer.iota.org/devnet/message/{message_id['message_id']}")




