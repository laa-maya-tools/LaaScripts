import base64

message = "Python is fun"
message_bytes = message.encode('latin_1')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('latin_1')

print(message_bytes)
print(base64_bytes)
print(base64_message)