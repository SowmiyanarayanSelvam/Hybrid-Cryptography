from ecies.utils import generate_key
from ecies import encrypt, decrypt

class ECC:

    def __init__(self):
        self.key = generate_key()
        self.priv_key = self.key.secret
        self.pub_key = self.key.public_key.format(True)

    def get_public_key(self):
        return self.pub_key

    def ECCencrypt(self, plaintext, publickey):
        #converting string to binary
        bin = bytes(plaintext, 'utf-8')

        #print(bin)

        #encrypting the data
        return encrypt(publickey, bin)

    def ECCdecrypt(self, ciphertext):

        return decrypt(self.priv_key, ciphertext).decode('utf-8')

e1 = ECC()
e2 = ECC()

print(e2.ECCdecrypt((e1.ECCencrypt("DMJ", e2.get_public_key()))))
