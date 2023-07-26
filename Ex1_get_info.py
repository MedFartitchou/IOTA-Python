# In this example, a new IOTA Client object instance is created, and it displays the node information of the connected node.
import iota_client

# Chrysalis testnet node
client = iota_client.Client(
    nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])
print(client.get_info())
