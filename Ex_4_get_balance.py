# In this example, we fetch the balance of the provided address as well as the total balance of the given seed.
import os
import iota_client

IOTA_SEED_SECRET = "e92ed03d9d4aef97538c379c6952dae9e56d22123b0e350d1c73777da1c42de7"
client = iota_client.Client(nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])

print("Return a balance for a single address:")
print(client.get_address_balance("atoi1qp9427varyc05py79ajku89xarfgkj74tpel5egr9y7xu3wpfc4lkpx0l86"))
print("Return a balance for the given seed and account_index:")
print(
    client.get_balance(
        seed=IOTA_SEED_SECRET,
        account_index=0,
        initial_address_index=0
    ))
