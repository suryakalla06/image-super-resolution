# The Final Project

## Part 2 - RSA Digital Signatures

Write a script called ```sign.py``` that takes in a the name of a text file as input and prints out the digital signature of that file as follows:
- It must first get the SHA-256 hash of the file (as bytes).
- Then it must create a random semiprime `N` to be used in the RSA digital signature.
- Then it signs the hash using RSA digital signature with `N` above and `e = 65537`.
- Finally, it returns `(N, e)` as a tuple and the the signature (in hex)

Create a separate script called ```verifier.py``` that takes in tha name of a text file, N, e, and a signature in hex and verifies the digital signature of the contents of the text file and returns ```accept``` or ```reject``` depending on whether the signature is valid or not.

### Running Instructions

Run the file sign.py using the terminal and provide the name of file whose RSA Digital Signature has to be generated as an argument.
    Syntax:
        python3 sign.py <file name>

Run the file verifier.py using the terminal and provide the name of file whose RSA Digital Signature has to be verified along with n, e and the siganture as an argument. The output i.e. 'accept' or 'reject' will be printed on terminal
    Syntax:
        python3 verifier.py <file name> n e signature
