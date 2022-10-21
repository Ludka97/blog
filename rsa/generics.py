from Crypto.PublicKey import RSA

key_pair = RSA.generate(2048)
print("Public key:", key_pair.public_key().export_key())
print("Private key:", key_pair.export_key())
