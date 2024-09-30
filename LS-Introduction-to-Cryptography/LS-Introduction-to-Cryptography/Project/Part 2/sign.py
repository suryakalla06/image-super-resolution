import hashlib, random, sympy, sys

def generate_sha256_hash(input_string):
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha256_hash

def generate_random_semiprime(bits):
    while True:
        p = sympy.nextprime(random.getrandbits(bits))
        q = sympy.nextprime(random.getrandbits(bits))
        
        n = p * q
        if n.bit_length() == bits * 2:
            return n, p, q


def rsa_encrypt(n, e, message):
    # Step 1: Convert the message to an integer (using ASCII values in this example)
    integer_message = int.from_bytes(message.encode(), 'big')

    # Step 2: RSA encryption (ciphertext = message^e mod n)
    ciphertext = pow(integer_message, e, n)
    # Step 3: Convert to hexadecimal
    hex_ciphertext = hex(ciphertext)[2:]
    
    return hex_ciphertext

if __name__ == "__main__":

    file = sys.argv[1]
    with open(file, 'r') as f:
        input_data = f.read()
    

    semiprime, _, _ = generate_random_semiprime(120)
    e = 65537
    public_key = (semiprime, e)

    encrypted_message = rsa_encrypt(semiprime, e, generate_sha256_hash(input_data))
    print(public_key, encrypted_message)

