import base64

def encode_string(input_string):
    # Convert the string to bytes and encode it using base64
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    # Convert the encoded bytes back to a string and return it
    return encoded_bytes.decode('utf-8')

def decode_string(encoded_string):
    # Convert the encoded string to bytes and decode it using base64
    decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
    # Convert the decoded bytes back to a string and return it
    return decoded_bytes.decode('utf-8')

# Example usage
input_string = "Hello, this is a secret message!"
encoded = encode_string(input_string)
print("Encoded:", encoded)

decoded = decode_string(encoded)
print("Decoded:", decoded)
