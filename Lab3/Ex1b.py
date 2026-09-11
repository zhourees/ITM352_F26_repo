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
