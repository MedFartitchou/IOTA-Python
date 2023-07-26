# To retrieve Unspent Transaction Outputs (UTXOs) related to an address, you have three available functions:
    # Client.get_address_outputs(str)
    # Client.get_output(str)
    # Client.find_outputs(output_ids (optional), addresses (optional))

import iota_client
client = iota_client.Client(nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])

outputs = client.get_address_outputs("atoi1qp9427varyc05py79ajku89xarfgkj74tpel5egr9y7xu3wpfc4lkpx0l86")
for output in outputs:
    print(f"Output index: {output['index']}; raw transaction id: {output['transaction_id']}")
    encoded_hex = "".join(f"{i:0>2x}" for i in output["transaction_id"] + list(int(output["index"]).to_bytes(2, 'little')))
    print(f"`output_id` encoded in hex: {encoded_hex}")
