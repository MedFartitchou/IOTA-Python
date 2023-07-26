#This example demonstrates creating a data transaction split over multiple messages,
# which can be useful for handling large messages that exceed the 32,768-byte limit.
import iota_client

INDEX = "IOTA Network"
DATA = ("IOTA tokens!" * 10).encode() 
CHUNK_SIZE = 128  # Split into multiple 128 character messages
client = iota_client.Client(nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])
counter = 1
message_ids = []
while len(DATA):
    message_id_indexation = client.message(index=INDEX, data=DATA[:128])
    print('Message ' + str(counter) + " sent!")
    print("https://explorer.iota.org/devnet/message/" + message_id_indexation['message_id'])
    message_ids.append(message_id_indexation['message_id'])
    DATA = DATA[128:]
    counter += 1

print("\nCopy IDs of your messages. You'll need them in the next example.")
print(f'Message IDs: {str(message_ids)}')





