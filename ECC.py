from ecies.utils import generate_key
from ecies import encrypt, decrypt

class ECC:

    def __init__(self, verbosity):
        self.key = generate_key()
        self.priv_key = self.key.secret
        self.pub_key = self.key.public_key.format(True)
        self.verbosity = verbosity

        if(self.verbosity):
            print("Object of class ECC created")

    def get_public_key(self):
        if(self.verbosity):
            print("Sending public key from ECC object: " + str(self.pub_key))
        return self.pub_key

    def ECCencrypt(self, plaintext, publickey):
        #encrypting the data
        if(self.verbosity):
            print("Plain text has been ECC encrypted and returned")
        return encrypt(publickey, plaintext)

    def ECCdecrypt(self, ciphertext):
        #decrypting the ciphertext
        if(self.verbosity):
            print("Cipher text has been ECC decrypted and returned")
        return decrypt(self.priv_key, ciphertext).decode('utf-8')
