# In this example, the code fetches and prints a multi-transaction message.

import iota_client

# Replace the placeholders with the IDs obtained from the previous example.

MESSAGE_IDS = ['90cdf281cf44acdea4c3e7cc469267ea25b3b3230fad3a8b7b55bdc48b7c806f']

client = iota_client.Client(nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])
full_message = ""
for x in range(len(MESSAGE_IDS)):
    message = client.get_message_data(MESSAGE_IDS[x])
    message_index = message['payload']['indexation'][0]['index']
    message_content = message['payload']['indexation'][0]['data']
    full_message += bytes (message_content). decode()
    print(f'Message {x + 1} content: {bytes(message_content).decode()}')
    print(f'Message {x + 1} length: {len(bytes(message_content).decode())} bytes')
print(f'\nResulting message: {full_message}')
print(f'Resulting message length: {len(full_message)} bytes')






