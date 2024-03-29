import binascii

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

key_pair = RSA.importKey(
    """-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3XJCZowbem/rlo36hwP4\n
    CD+wCMiTlMHOPWlpDNfqf55kthjsEcEellcRlB0CGMP8Ea/gYo0yICIgFf710Phi\n
    36kuQlqbJGZj43py4v3yD2XQVuuQcx1WaM0AEo+hB8C8RmvQg8VKyE2Dy3MBTB3A\n
    OL2Qlg8lutepZ6IMR5n4WoltaMjiQp406R08JS4byUn6txJ7hbCVWMrEBVEdvplJ\n
    7Q3ovjGq1YUGtiNDd3IbiPcc6Ar5Zfr2DJ/AlF3lweT+78hya7yoZFh6O4ACNxY0\n
    wRDnegBcDFrheExxSwvDKi+lBOkbdLZq62A2AVyMLR48ESezo4RrgjJVmWy3MkB/\n
    lQIDAQAB\n-----END PUBLIC KEY-----"""
)

message = "A message for encryption".encode()
cipher = PKCS1_OAEP.new(key_pair)

encrypted = cipher.encrypt(message)
print("Encrypted:", binascii.hexlify(encrypted))

decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted.decode())
