from cryptography.fernet import Fernet;

key = Fernet.generate_key();
cypher_suite = Fernet(key);

encodedText = cypher_suite.encrypt(b"Hello world");
print("Encoded text:", encodedText);
decodedText = cypher_suite.decrypt(encodedText);
print("Decoded text:", decodedText);