from sign import rsa_encrypt, generate_sha256_hash
import sys

file = sys.argv[1]
with open(file, 'r') as f:
        input_data = f.read()
n = int(sys.argv[2])
e = int(sys.argv[3])
signature = (sys.argv[4])

encrypted_message = rsa_encrypt(n, e, generate_sha256_hash(input_data))

if signature == encrypted_message:
	print("accept")
else:
	print("reject")
	print(encrypted_message)