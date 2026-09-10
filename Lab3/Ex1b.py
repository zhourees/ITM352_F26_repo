# Imports Fernet to encrypt a string, then decrypts the same string
# Name: Reesa Zhou
# Date: September 9, 2026

from cryptography.fernet import Fernet;

key = Fernet.generate_key();
cypher_suite = Fernet(key);

encodedText = cypher_suite.encrypt(b"Hello world");
print("Encoded text:", encodedText);
decodedText = cypher_suite.decrypt(encodedText);
print("Decoded text:", decodedText);

# takes 1 parameter, parameters have their expected place (look at function signature)
# Fernet is not the only package that provides encryption. Other ones don't need the string as
# a parameter
# it's different because it assumes youll use the same key. other functions might have different
# keys, so youll have to use the right key