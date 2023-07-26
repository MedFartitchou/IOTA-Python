# Create IOTA address using Client.get_addresses() for a list of tuples with generated addresses.
import iota_client

client = iota_client.Client( nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])
# Insert your testing seed here.
IOTA_SEED = 'e92ed03d9d4aef97538c379c6952dae9e56d22123b0e350d1c73777da1c42de7'
address_changed_list = client.get_addresses(
    seed=IOTA_SEED,
    account_index=0,
    input_range_begin=0,
    input_range_end=10,
    get_all=True
)
print(address_changed_list)



