import base64

base64_message = 'bGljZW5zaW5nV2luZG93'
base64_bytes = base64_message.encode('latin_1')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('latin_1')

print(message)